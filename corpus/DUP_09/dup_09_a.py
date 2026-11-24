def extremos_vendas(lista):
    maior = lista[0]
    menor = lista[0]
    for x in lista:
        if x > maior:
            maior = x
        if x < menor:
            menor = x
    return maior, menor
