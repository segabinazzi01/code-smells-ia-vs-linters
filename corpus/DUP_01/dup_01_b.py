def preco_servico(preco, quantidade):
    desconto = preco * 0.10
    if quantidade >= 10:
        desconto = desconto + preco * 0.05
    valor_final = preco - desconto
    valor_final = round(valor_final, 2)
    return valor_final
