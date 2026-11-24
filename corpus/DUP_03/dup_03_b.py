def total_orcamento(itens):
    total = 0
    for item in itens:
        total = total + item['preco'] * item['qtd']
    imposto = total * 0.18
    total = total + imposto
    return round(total, 2)
