def gerar_relatorio(
    titulo,
    autor,
    data_inicio,
    data_fim,
    formato,
    filtro,
    ordenacao,
    limite
):
    registro = {
        "titulo": titulo,
        "autor": autor,
        "data_inicio": data_inicio,
        "data_fim": data_fim,
        "formato": formato,
        "filtro": filtro,
        "ordenacao": ordenacao,
        "limite": limite,
    }
    return registro
