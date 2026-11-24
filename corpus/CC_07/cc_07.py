def liberar_saque(conta):
    if conta is not None:
        if conta.ativa:
            if conta.saldo > 0:
                if not conta.bloqueada:
                    if conta.limite_diario > 0:
                        if conta.token_valido:
                            return True
    return False
