def validar_cpf_funcionario(cpf):
    cpf = ''.join(c for c in cpf if c.isdigit())
    if len(cpf) != 11:
        return False
    if cpf == cpf[0] * 11:
        return False
    return True
