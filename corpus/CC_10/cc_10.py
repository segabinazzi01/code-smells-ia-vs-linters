def liberar_deploy(release):
    if release is not None:
        if release.testes_ok:
            if release.revisada:
                if release.sem_vulnerabilidade:
                    if release.aprovada_po:
                        if release.janela_livre:
                            if release.rollback_pronto:
                                return True
    return False
