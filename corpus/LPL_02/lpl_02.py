def criar_pedido(
    cliente_id,
    produto_id,
    quantidade,
    preco,
    desconto,
    frete,
    forma_pagamento
):
    registro = {
        "cliente_id": cliente_id,
        "produto_id": produto_id,
        "quantidade": quantidade,
        "preco": preco,
        "desconto": desconto,
        "frete": frete,
        "forma_pagamento": forma_pagamento,
    }
    return registro
