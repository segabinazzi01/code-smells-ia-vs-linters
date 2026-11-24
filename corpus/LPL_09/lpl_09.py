def emitir_nota(
    numero,
    cliente,
    itens,
    valor_total,
    imposto,
    data_emissao,
    serie,
    natureza,
    observacao
):
    registro = {
        "numero": numero,
        "cliente": cliente,
        "itens": itens,
        "valor_total": valor_total,
        "imposto": imposto,
        "data_emissao": data_emissao,
        "serie": serie,
        "natureza": natureza,
        "observacao": observacao,
    }
    return registro
