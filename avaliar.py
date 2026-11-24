"""Calcula precisao, recall, F1 e estabilidade (Pylint e LLM).

Uso: python avaliar.py [resultados/llm_bruto.jsonl]
"""
import csv
import glob
import json
import subprocess
import sys
from collections import defaultdict

TIPOS = ["LPL", "DUP", "CC"]
SIMBOLOS = {"too-many-arguments": "LPL", "duplicate-code": "DUP",
            "too-many-nested-blocks": "CC"}


def normalizar(texto):
    t = (texto or "").lower()
    if "parameter" in t or "parâmetro" in t:
        return "LPL"
    if "duplicate" in t or "duplicado" in t or "duplicação" in t:
        return "DUP"
    if "conditional" in t or "condicional" in t:
        return "CC"
    return None


def metricas(prev, gab, ids):
    linhas = []
    for tp_ in TIPOS:
        tp = sum(1 for i in ids if tp_ in prev[i] and gab[i] == tp_)
        fp = sum(1 for i in ids if tp_ in prev[i] and gab[i] != tp_)
        fn = sum(1 for i in ids if tp_ not in prev[i] and gab[i] == tp_)
        p = tp / (tp + fp) if tp + fp else None
        r = tp / (tp + fn) if tp + fn else None
        f1 = 2 * p * r / (p + r) if p and r else (0.0 if p is not None
                                                  and r is not None else None)
        linhas.append((tp_, tp, fp, fn, p, r, f1))
    return linhas


def fmt(x):
    return "-" if x is None else f"{x:.2f}"


def main():
    arq = sys.argv[1] if len(sys.argv) > 1 else "resultados/llm_bruto.jsonl"
    gab = {}
    for r in csv.DictReader(open("corpus/gabarito.csv", encoding="utf-8")):
        gab[r["id"]] = r["tipo"]
    ids = list(gab)

    # --- Pylint ---
    pyl = {}
    for tid in ids:
        arqs = sorted(glob.glob(f"corpus/{tid}/*.py"))
        r = subprocess.run(["pylint", "--rcfile=pylintrc",
                            "--output-format=json", *arqs],
                           capture_output=True, text=True)
        msgs = json.loads(r.stdout or "[]")
        pyl[tid] = {SIMBOLOS[m["symbol"]] for m in msgs
                    if m["symbol"] in SIMBOLOS}

    # --- LLM ---
    por_trecho = defaultdict(list)
    falhas = 0
    for linha in open(arq, encoding="utf-8"):
        d = json.loads(linha)
        tipos = set()
        if d["parse_ok"]:
            for a in d["alertas"]:
                t = normalizar(a.get("tipo") if isinstance(a, dict) else "")
                if t:
                    tipos.add(t)
        else:
            falhas += 1
        por_trecho[d["id"]].append(tipos)

    llm, estab = {}, defaultdict(list)
    for tid in ids:
        runs = por_trecho.get(tid, [])
        n = len(runs)
        llm[tid] = set()
        for t in TIPOS:
            c = sum(1 for r in runs if t in r)
            if n and c > n / 2:
                llm[tid].add(t)
            if n:
                estab[t].append(max(c, n - c) / n)

    saida = []
    for nome, prev in (("Pylint", pyl), ("LLM", llm)):
        print(f"\n== {nome} ==")
        print("tipo   TP  FP  FN  precisao  recall    F1")
        for t, tp, fp, fn, p, r, f1 in metricas(prev, gab, ids):
            print(f"{t:<5} {tp:>3} {fp:>3} {fn:>3}  {fmt(p):>8} {fmt(r):>7} "
                  f"{fmt(f1):>5}")
            saida.append([nome, t, tp, fp, fn, fmt(p), fmt(r), fmt(f1)])

    print("\n== Estabilidade do LLM (media por tipo) ==")
    for t in TIPOS:
        v = estab[t]
        m = sum(v) / len(v) if v else None
        print(f"{t}: {fmt(m)}")
        saida.append(["Estabilidade", t, "", "", "", "", "", fmt(m)])
    print(f"\nRespostas com JSON invalido: {falhas}")

    with open("resultados/metricas.csv", "w", newline="",
              encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["ferramenta", "tipo", "TP", "FP", "FN", "precisao",
                    "recall", "F1"])
        w.writerows(saida)


if __name__ == "__main__":
    main()
