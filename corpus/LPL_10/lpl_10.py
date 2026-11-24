def matricular_aluno(
    nome,
    matricula,
    curso,
    semestre,
    turno,
    bolsa,
    email
):
    registro = {
        "nome": nome,
        "matricula": matricula,
        "curso": curso,
        "semestre": semestre,
        "turno": turno,
        "bolsa": bolsa,
        "email": email,
    }
    return registro
