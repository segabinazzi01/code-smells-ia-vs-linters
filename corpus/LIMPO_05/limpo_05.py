def aplicar_desconto(preco, percentual):
    desconto = preco * percentual
    return preco - desconto


def preco_produto(preco):
    return aplicar_desconto(preco, 0.10)


def preco_servico(preco):
    return aplicar_desconto(preco, 0.10)
