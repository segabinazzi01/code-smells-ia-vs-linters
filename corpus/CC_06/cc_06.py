def pode_matricular(aluno):
    if aluno is not None:
        if aluno.documentos_ok:
            if aluno.vaga_disponivel:
                if not aluno.debito:
                    if aluno.semestre <= 8:
                        return True
    return False
