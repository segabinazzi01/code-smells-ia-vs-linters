def aprovar_credito(cliente):
    if cliente is not None:
        if cliente.renda > 2000:
            if cliente.score > 600:
                if not cliente.negativado:
                    return True
    return False
