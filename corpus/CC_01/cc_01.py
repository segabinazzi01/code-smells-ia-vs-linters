def verificar_usuario(usuario):
    if usuario is not None:
        if usuario.ativo:
            if usuario.idade >= 18:
                if usuario.email is not None:
                    return True
    return False
