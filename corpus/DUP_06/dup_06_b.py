def ler_data_matricula(data):
    partes = data.split('/')
    dia = int(partes[0])
    mes = int(partes[1])
    ano = int(partes[2])
    if mes < 1 or mes > 12:
        raise ValueError('mes invalido')
    return ano, mes, dia
