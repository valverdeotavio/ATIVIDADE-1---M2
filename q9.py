def calcular_preco_final(preco: float, vip: bool) -> float:
    if preco >= 100:
        desconto = 0.20
    elif preco >= 50:
        desconto = 0.10
    else:
        desconto = 0.0

    if vip:
        desconto += 0.05

    return preco * (1 - desconto)