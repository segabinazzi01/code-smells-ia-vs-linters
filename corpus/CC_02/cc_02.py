def pode_emprestar(livro):
    if livro is not None:
        if livro.disponivel:
            if not livro.reservado:
                if livro.estado != 'danificado':
                    return True
    return False
