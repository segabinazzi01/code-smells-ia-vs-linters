"""Roda o LLM (Groq) em todos os trechos do corpus, N vezes cada.

Uso:
  export GROQ_API_KEY="sua_chave"      (Windows: set GROQ_API_KEY=sua_chave)
  python rodar_llm.py                  # roda tudo (retoma de onde parou)
  python rodar_llm.py --simular        # teste sem API e sem chave
"""
import argparse
import csv
import glob
import json
import os
import random
import re
import time
from datetime import datetime

import requests

# ---- Parametros do estudo (declarar na Metodologia) --------------------
MODELO = "openai/gpt-oss-120b"   # confira o ID em console.groq.com/docs/models
URL = "https://api.groq.com/openai/v1/chat/completions"
EXECUCOES = 5                    # execucoes por trecho
SEMENTE = 42                     # semente do sorteio da ordem
TEMPERATURA = None               # None = padrao do servico (nao enviado)
MAX_TOKENS = 4000
# -------------------------------------------------------------------------

SAIDA = "resultados/llm_bruto.jsonl"
MARCADOR = "<COLAR O(S) ARQUIVO(S) DO TRECHO AQUI>"


def carregar_ids():
    with open("corpus/gabarito.csv", encoding="utf-8") as f:
        return [(r["id"], r["tipo"]) for r in csv.DictReader(f)]


def montar_prompt(tid):
    base = open("prompt.txt", encoding="utf-8").read()
    partes = []
    for caminho in sorted(glob.glob(f"corpus/{tid}/*.py")):
        codigo = open(caminho, encoding="utf-8").read()
        partes.append(f"### arquivo: {os.path.basename(caminho)}\n{codigo}")
    return base.replace(MARCADOR, "\n".join(partes))


def chamar_api(prompt, chave):
    corpo = {
        "model": MODELO,
        "messages": [{"role": "user", "content": prompt}],
        "max_completion_tokens": MAX_TOKENS,
    }
    if TEMPERATURA is not None:
        corpo["temperature"] = TEMPERATURA
    cab = {"Authorization": f"Bearer {chave}"}
    for tentativa in range(7):
        r = requests.post(URL, headers=cab, json=corpo, timeout=120)
        if r.status_code == 200:
            d = r.json()
            return d["choices"][0]["message"].get("content") or "", d.get("model")
        if r.status_code in (429, 500, 502, 503):
            espera = float(r.headers.get("retry-after", 5 * 2 ** tentativa))
            print(f"  aguardando {espera:.0f}s (HTTP {r.status_code})")
            time.sleep(espera)
            continue
        raise RuntimeError(f"HTTP {r.status_code}: {r.text[:300]}")
    raise RuntimeError("muitas tentativas falharam")


def simular(tipo):
    """Resposta falsa so para testar o pipeline (NAO usar no estudo)."""
    nomes = {"LPL": "Long Parameter List", "DUP": "Duplicate Code",
             "CC": "Complex Conditional"}
    if tipo in nomes and random.random() < 0.8:
        return json.dumps([{"tipo": nomes[tipo], "arquivo": "x.py",
                            "linhas": "1-5", "justificativa": "simulado"}])
    return "[]"


def extrair_json(texto):
    t = re.sub(r"```(?:json)?", "", texto)
    i, j = t.find("["), t.rfind("]")
    if i == -1 or j == -1 or j < i:
        return None
    try:
        dados = json.loads(t[i:j + 1])
        return dados if isinstance(dados, list) else None
    except json.JSONDecodeError:
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    args = ap.parse_args()

    chave = os.environ.get("GROQ_API_KEY")
    if not chave and not args.simular:
        raise SystemExit("Defina a variavel de ambiente GROQ_API_KEY.")

    saida = SAIDA.replace(".jsonl", "_simulado.jsonl") if args.simular else SAIDA
    os.makedirs("resultados", exist_ok=True)

    ids = carregar_ids()
    tipos = dict(ids)
    pares = [(tid, k) for tid, _ in ids for k in range(1, EXECUCOES + 1)]
    random.Random(SEMENTE).shuffle(pares)

    feitos = set()
    if os.path.exists(saida):
        for linha in open(saida, encoding="utf-8"):
            d = json.loads(linha)
            feitos.add((d["id"], d["execucao"]))

    with open("resultados/meta.json", "w", encoding="utf-8") as f:
        json.dump({"modelo": MODELO, "execucoes": EXECUCOES,
                   "semente": SEMENTE, "temperatura": TEMPERATURA,
                   "max_tokens": MAX_TOKENS,
                   "inicio": datetime.now().isoformat(timespec="seconds")},
                  f, indent=2)

    with open(saida, "a", encoding="utf-8") as out:
        for ordem, (tid, k) in enumerate(pares, start=1):
            if (tid, k) in feitos:
                continue
            print(f"[{ordem}/{len(pares)}] {tid} execucao {k}")
            if args.simular:
                texto, modelo_real = simular(tipos[tid]), "simulado"
            else:
                texto, modelo_real = chamar_api(montar_prompt(tid), chave)
                time.sleep(1)
            alertas = extrair_json(texto)
            out.write(json.dumps({
                "id": tid, "execucao": k, "ordem": ordem,
                "modelo_retornado": modelo_real,
                "data_hora": datetime.now().isoformat(timespec="seconds"),
                "resposta_bruta": texto, "alertas": alertas,
                "parse_ok": alertas is not None,
            }, ensure_ascii=False) + "\n")
            out.flush()
    print("Concluido ->", saida)


if __name__ == "__main__":
    main()
