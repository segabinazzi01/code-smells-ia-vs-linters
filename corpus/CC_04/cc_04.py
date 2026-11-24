def liberar_acesso(pessoa):
    if pessoa is not None:
        if pessoa.cadastro_ok:
            if pessoa.cracha_valido:
                if pessoa.setor == 'ti':
                    if pessoa.turno == 'dia':
                        return True
    return False
