def gerar_codigo_produto(nome, numero, usados):
    prefixo = nome[:3].upper()
    sufixo = str(numero).zfill(4)
    codigo = prefixo + '-' + sufixo
    if codigo in usados:
        codigo = codigo + '-B'
    return codigo
