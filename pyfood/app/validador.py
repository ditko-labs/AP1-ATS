def validar_pedido(pedido: dict) -> bool:
    if len(pedido["itens"]) < 1:
        return False

    total = 0
    for item in pedido["itens"]:
        total += item["preco"]

    if total < 20:
        return False

    if "endereco_entrega" not in pedido or pedido["endereco_entrega"] == "":
        return False

    return True