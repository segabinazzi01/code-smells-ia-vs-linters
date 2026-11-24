def contar_pares_positivos(matriz):
    total = 0
    for linha in matriz:
        for valor in linha:
            if valor > 0 and valor % 2 == 0:
                total += 1
    return total
