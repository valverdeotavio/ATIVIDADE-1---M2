def classificar_triangulo(lado1: float, lado2: float, lado3: float) -> str:
    if lado1 == lado2 and lado1 == lado3:
        return "Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return "Isósceles"
    else:
        return "Escaleno"