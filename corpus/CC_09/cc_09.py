def autorizar_viagem(viajante):
    if viajante is not None:
        if viajante.passaporte_ok:
            if viajante.visto_ok:
                if not viajante.restricao:
                    if viajante.seguro:
                        if viajante.bagagem_ok:
                            if viajante.checkin:
                                return True
    return False
