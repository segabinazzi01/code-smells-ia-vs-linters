def verificar_usuario(usuario):
    if usuario is None:
        return False
    if not usuario.ativo:
        return False
    if usuario.idade < 18:
        return False
    if usuario.email is None:
        return False
    return True
