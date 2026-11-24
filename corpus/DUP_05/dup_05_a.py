def media_turma_a(notas):
    soma = 0
    for nota in notas:
        soma = soma + nota
    media = soma / len(notas)
    situacao = 'aprovado' if media >= 6 else 'reprovado'
    return media, situacao
