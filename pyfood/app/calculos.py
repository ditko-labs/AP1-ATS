def calcular_total_com_desconto(pedido: dict) -> float: 
    total = 0
    for item in pedido["itens"]:
        total += item["preco"]
    if total > 100:
        total = total * 0.9

    return total