"""Gera o corpus do experimento: 35 trechos em Python + gabarito.csv.

Tipos: LPL (Long Parameter List), DUP (Duplicate Code),
       CC (Complex Conditional) e LIMPO (sem smell).
Cada trecho fica em corpus/<id>/ (DUP tem 2 arquivos).
"""
import csv
import os
import shutil

RAIZ = "corpus"
gabarito = []  # (id, tipo, arquivos, linhas, descricao)


def salvar(pasta, nome, linhas):
    caminho = os.path.join(RAIZ, pasta)
    os.makedirs(caminho, exist_ok=True)
    with open(os.path.join(caminho, nome), "w", encoding="utf-8") as f:
        f.write("\n".join(linhas) + "\n")


# ---------------------------------------------------------------
# 1) LONG PARAMETER LIST: 10 funcoes com 6 a 10 parametros
# ---------------------------------------------------------------
LPL = [
    ("cadastrar_cliente", ["nome", "idade", "cpf", "endereco", "cidade",
                           "estado", "cep", "telefone", "email"]),
    ("criar_pedido", ["cliente_id", "produto_id", "quantidade", "preco",
                      "desconto", "frete", "forma_pagamento"]),
    ("enviar_email", ["remetente", "destinatario", "assunto", "corpo",
                      "anexo", "copia", "prioridade", "assinatura"]),
    ("gerar_relatorio", ["titulo", "autor", "data_inicio", "data_fim",
                         "formato", "filtro", "ordenacao", "limite"]),
    ("agendar_consulta", ["paciente", "medico", "data", "hora",
                          "sala", "convenio", "observacao"]),
    ("registrar_produto", ["nome", "categoria", "preco", "estoque",
                           "fornecedor", "codigo_barras", "peso",
                           "validade", "marca", "descricao"]),
    ("calcular_frete", ["origem", "destino", "peso", "altura", "largura",
                        "comprimento", "urgente"]),
    ("criar_usuario", ["login", "senha", "nome", "email", "perfil",
                       "ativo", "data_criacao", "idioma"]),
    ("emitir_nota", ["numero", "cliente", "itens", "valor_total", "imposto",
                     "data_emissao", "serie", "natureza", "observacao"]),
    ("matricular_aluno", ["nome", "matricula", "curso", "semestre",
                          "turno", "bolsa", "email"]),
]

for i, (nome, params) in enumerate(LPL, start=1):
    tid = f"LPL_{i:02d}"
    linhas = [f"def {nome}("]
    linhas += [f"    {p}," for p in params[:-1]]
    linhas += [f"    {params[-1]}", "):"]
    linhas += ["    registro = {"]
    linhas += [f'        "{p}": {p},' for p in params]
    linhas += ["    }", "    return registro"]
    salvar(tid, f"{tid.lower()}.py", linhas)
    fim = len(linhas)
    gabarito.append((tid, "LPL", f"{tid.lower()}.py", f"1-{fim}",
                     f"{nome} recebe {len(params)} parametros"))

# ---------------------------------------------------------------
# 2) COMPLEX CONDITIONAL: 10 funcoes com ifs aninhados (4 a 7 niveis)
# ---------------------------------------------------------------
CC = [
    ("verificar_usuario", "usuario",
     ["usuario is not None", "usuario.ativo", "usuario.idade >= 18",
      "usuario.email is not None"]),
    ("pode_emprestar", "livro",
     ["livro is not None", "livro.disponivel", "not livro.reservado",
      "livro.estado != 'danificado'"]),
    ("aprovar_credito", "cliente",
     ["cliente is not None", "cliente.renda > 2000", "cliente.score > 600",
      "not cliente.negativado"]),
    ("liberar_acesso", "pessoa",
     ["pessoa is not None", "pessoa.cadastro_ok", "pessoa.cracha_valido",
      "pessoa.setor == 'ti'", "pessoa.turno == 'dia'"]),
    ("validar_pedido", "pedido",
     ["pedido is not None", "pedido.itens", "pedido.pagamento_ok",
      "pedido.endereco is not None", "pedido.total > 0"]),
    ("pode_matricular", "aluno",
     ["aluno is not None", "aluno.documentos_ok", "aluno.vaga_disponivel",
      "not aluno.debito", "aluno.semestre <= 8"]),
    ("liberar_saque", "conta",
     ["conta is not None", "conta.ativa", "conta.saldo > 0",
      "not conta.bloqueada", "conta.limite_diario > 0",
      "conta.token_valido"]),
    ("aceitar_inscricao", "candidato",
     ["candidato is not None", "candidato.idade >= 16",
      "candidato.cpf_valido", "candidato.pagou", "candidato.vaga",
      "not candidato.duplicado"]),
    ("autorizar_viagem", "viajante",
     ["viajante is not None", "viajante.passaporte_ok",
      "viajante.visto_ok", "not viajante.restricao", "viajante.seguro",
      "viajante.bagagem_ok", "viajante.checkin"]),
    ("liberar_deploy", "release",
     ["release is not None", "release.testes_ok", "release.revisada",
      "release.sem_vulnerabilidade", "release.aprovada_po",
      "release.janela_livre", "release.rollback_pronto"]),
]

for i, (nome, arg, conds) in enumerate(CC, start=1):
    tid = f"CC_{i:02d}"
    linhas = [f"def {nome}({arg}):"]
    for nivel, c in enumerate(conds, start=1):
        linhas.append("    " * nivel + f"if {c}:")
    linhas.append("    " * (len(conds) + 1) + "return True")
    linhas.append("    return False")
    salvar(tid, f"{tid.lower()}.py", linhas)
    gabarito.append((tid, "CC", f"{tid.lower()}.py", f"1-{len(linhas)}",
                     f"{nome} com {len(conds)} niveis de if aninhado"))

# ---------------------------------------------------------------
# 3) DUPLICATE CODE: 10 pares de arquivos com bloco identico
# ---------------------------------------------------------------
BLOCOS = [
    ["    desconto = preco * 0.10",
     "    if quantidade >= 10:",
     "        desconto = desconto + preco * 0.05",
     "    valor_final = preco - desconto",
     "    valor_final = round(valor_final, 2)",
     "    return valor_final"],
    ["    texto = texto.strip()",
     "    texto = texto.lower()",
     "    texto = texto.replace('  ', ' ')",
     "    if len(texto) > 50:",
     "        texto = texto[:50]",
     "    return texto"],
    ["    total = 0",
     "    for item in itens:",
     "        total = total + item['preco'] * item['qtd']",
     "    imposto = total * 0.18",
     "    total = total + imposto",
     "    return round(total, 2)"],
    ["    if valor is None:",
     "        raise ValueError('valor ausente')",
     "    if valor < 0:",
     "        raise ValueError('valor negativo')",
     "    if valor > 10000:",
     "        raise ValueError('valor acima do limite')",
     "    return valor"],
    ["    soma = 0",
     "    for nota in notas:",
     "        soma = soma + nota",
     "    media = soma / len(notas)",
     "    situacao = 'aprovado' if media >= 6 else 'reprovado'",
     "    return media, situacao"],
    ["    partes = data.split('/')",
     "    dia = int(partes[0])",
     "    mes = int(partes[1])",
     "    ano = int(partes[2])",
     "    if mes < 1 or mes > 12:",
     "        raise ValueError('mes invalido')",
     "    return ano, mes, dia"],
    ["    resultado = []",
     "    for linha in linhas:",
     "        linha = linha.strip()",
     "        if linha and not linha.startswith('#'):",
     "            resultado.append(linha)",
     "    return resultado"],
    ["    cpf = ''.join(c for c in cpf if c.isdigit())",
     "    if len(cpf) != 11:",
     "        return False",
     "    if cpf == cpf[0] * 11:",
     "        return False",
     "    return True"],
    ["    maior = lista[0]",
     "    menor = lista[0]",
     "    for x in lista:",
     "        if x > maior:",
     "            maior = x",
     "        if x < menor:",
     "            menor = x",
     "    return maior, menor"],
    ["    prefixo = nome[:3].upper()",
     "    sufixo = str(numero).zfill(4)",
     "    codigo = prefixo + '-' + sufixo",
     "    if codigo in usados:",
     "        codigo = codigo + '-B'",
     "    return codigo"],
]
# assinatura e variaveis esperadas por bloco (para o codigo ficar valido)
ASSIN = [
    ("preco, quantidade", "preco, quantidade"),
    ("texto", "texto"),
    ("itens", "itens"),
    ("valor", "valor"),
    ("notas", "notas"),
    ("data", "data"),
    ("linhas", "linhas"),
    ("cpf", "cpf"),
    ("lista", "lista"),
    ("nome, numero, usados", "nome, numero, usados"),
]
NOMES = [
    ("preco_produto", "preco_servico"),
    ("normalizar_titulo", "normalizar_comentario"),
    ("total_pedido", "total_orcamento"),
    ("validar_pagamento", "validar_saque"),
    ("media_turma_a", "media_turma_b"),
    ("ler_data_nascimento", "ler_data_matricula"),
    ("limpar_log", "limpar_config"),
    ("validar_cpf_cliente", "validar_cpf_funcionario"),
    ("extremos_vendas", "extremos_temperaturas"),
    ("gerar_codigo_produto", "gerar_codigo_cliente"),
]

for i, bloco in enumerate(BLOCOS, start=1):
    tid = f"DUP_{i:02d}"
    args = ASSIN[i - 1][0]
    nome_a, nome_b = NOMES[i - 1]
    arqs = []
    inicio = None
    for sufixo, nome in (("a", nome_a), ("b", nome_b)):
        linhas = [f"def {nome}({args}):"] + bloco
        arq = f"{tid.lower()}_{sufixo}.py"
        salvar(tid, arq, linhas)
        arqs.append(arq)
    gabarito.append((tid, "DUP", "+".join(arqs), f"2-{len(bloco) + 1}",
                     f"bloco de {len(bloco)} linhas identico nos dois "
                     f"arquivos"))

# ---------------------------------------------------------------
# 4) LIMPO: 5 trechos sem smell (2 deles no limite dos limiares)
# ---------------------------------------------------------------
LIMPOS = {
    "LIMPO_01": [
        "def calcular_area(largura, altura):",
        "    if largura <= 0 or altura <= 0:",
        "        raise ValueError('medidas invalidas')",
        "    return largura * altura",
    ],
    "LIMPO_02": [  # exatamente 5 parametros (limite do Pylint)
        "def criar_contato(nome, email, telefone, cidade, estado):",
        "    return {",
        '        "nome": nome,',
        '        "email": email,',
        '        "telefone": telefone,',
        '        "cidade": cidade,',
        '        "estado": estado,',
        "    }",
    ],
    "LIMPO_03": [  # 3 niveis de aninhamento (abaixo do smell)
        "def contar_pares_positivos(matriz):",
        "    total = 0",
        "    for linha in matriz:",
        "        for valor in linha:",
        "            if valor > 0 and valor % 2 == 0:",
        "                total += 1",
        "    return total",
    ],
    "LIMPO_04": [  # versao refatorada com retornos antecipados
        "def verificar_usuario(usuario):",
        "    if usuario is None:",
        "        return False",
        "    if not usuario.ativo:",
        "        return False",
        "    if usuario.idade < 18:",
        "        return False",
        "    if usuario.email is None:",
        "        return False",
        "    return True",
    ],
    "LIMPO_05": [  # logica compartilhada em uma unica funcao
        "def aplicar_desconto(preco, percentual):",
        "    desconto = preco * percentual",
        "    return preco - desconto",
        "",
        "",
        "def preco_produto(preco):",
        "    return aplicar_desconto(preco, 0.10)",
        "",
        "",
        "def preco_servico(preco):",
        "    return aplicar_desconto(preco, 0.10)",
    ],
}
for tid, linhas in LIMPOS.items():
    salvar(tid, f"{tid.lower()}.py", linhas)
    gabarito.append((tid, "LIMPO", f"{tid.lower()}.py", "-",
                     "sem smell planejado"))

with open(os.path.join(RAIZ, "gabarito.csv"), "w", newline="",
          encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["id", "tipo", "arquivos", "linhas", "descricao"])
    w.writerows(gabarito)

print(len(gabarito), "trechos gerados")
