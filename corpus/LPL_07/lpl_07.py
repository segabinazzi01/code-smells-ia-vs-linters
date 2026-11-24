def calcular_frete(
    origem,
    destino,
    peso,
    altura,
    largura,
    comprimento,
    urgente
):
    registro = {
        "origem": origem,
        "destino": destino,
        "peso": peso,
        "altura": altura,
        "largura": largura,
        "comprimento": comprimento,
        "urgente": urgente,
    }
    return registro
