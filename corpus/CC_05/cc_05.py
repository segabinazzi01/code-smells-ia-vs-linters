def validar_pedido(pedido):
    if pedido is not None:
        if pedido.itens:
            if pedido.pagamento_ok:
                if pedido.endereco is not None:
                    if pedido.total > 0:
                        return True
    return False
