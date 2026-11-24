def calcular_area(largura, altura):
    if largura <= 0 or altura <= 0:
        raise ValueError('medidas invalidas')
    return largura * altura
