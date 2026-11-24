def limpar_log(linhas):
    resultado = []
    for linha in linhas:
        linha = linha.strip()
        if linha and not linha.startswith('#'):
            resultado.append(linha)
    return resultado
