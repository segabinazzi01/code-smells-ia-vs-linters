def enviar_email(
    remetente,
    destinatario,
    assunto,
    corpo,
    anexo,
    copia,
    prioridade,
    assinatura
):
    registro = {
        "remetente": remetente,
        "destinatario": destinatario,
        "assunto": assunto,
        "corpo": corpo,
        "anexo": anexo,
        "copia": copia,
        "prioridade": prioridade,
        "assinatura": assinatura,
    }
    return registro
