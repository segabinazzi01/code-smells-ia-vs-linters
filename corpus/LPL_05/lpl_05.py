def agendar_consulta(
    paciente,
    medico,
    data,
    hora,
    sala,
    convenio,
    observacao
):
    registro = {
        "paciente": paciente,
        "medico": medico,
        "data": data,
        "hora": hora,
        "sala": sala,
        "convenio": convenio,
        "observacao": observacao,
    }
    return registro
