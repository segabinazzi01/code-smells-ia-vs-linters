def aceitar_inscricao(candidato):
    if candidato is not None:
        if candidato.idade >= 16:
            if candidato.cpf_valido:
                if candidato.pagou:
                    if candidato.vaga:
                        if not candidato.duplicado:
                            return True
    return False
