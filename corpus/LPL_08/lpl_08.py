def criar_usuario(
    login,
    senha,
    nome,
    email,
    perfil,
    ativo,
    data_criacao,
    idioma
):
    registro = {
        "login": login,
        "senha": senha,
        "nome": nome,
        "email": email,
        "perfil": perfil,
        "ativo": ativo,
        "data_criacao": data_criacao,
        "idioma": idioma,
    }
    return registro
