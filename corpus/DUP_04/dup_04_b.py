def validar_saque(valor):
    if valor is None:
        raise ValueError('valor ausente')
    if valor < 0:
        raise ValueError('valor negativo')
    if valor > 10000:
        raise ValueError('valor acima do limite')
    return valor
