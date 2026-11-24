def cadastrar_cliente(
    nome,
    idade,
    cpf,
    endereco,
    cidade,
    estado,
    cep,
    telefone,
    email
):
    registro = {
        "nome": nome,
        "idade": idade,
        "cpf": cpf,
        "endereco": endereco,
        "cidade": cidade,
        "estado": estado,
        "cep": cep,
        "telefone": telefone,
        "email": email,
    }
    return registro
