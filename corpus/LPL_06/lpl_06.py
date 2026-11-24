def registrar_produto(
    nome,
    categoria,
    preco,
    estoque,
    fornecedor,
    codigo_barras,
    peso,
    validade,
    marca,
    descricao
):
    registro = {
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "estoque": estoque,
        "fornecedor": fornecedor,
        "codigo_barras": codigo_barras,
        "peso": peso,
        "validade": validade,
        "marca": marca,
        "descricao": descricao,
    }
    return registro
