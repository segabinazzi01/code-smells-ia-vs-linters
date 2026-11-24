def normalizar_comentario(texto):
    texto = texto.strip()
    texto = texto.lower()
    texto = texto.replace('  ', ' ')
    if len(texto) > 50:
        texto = texto[:50]
    return texto
