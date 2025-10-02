def calcular_bonus(salario: float, tempo: int) -> float:
    if salario < 2000 and tempo >= 5:
        return salario * 0.2
    elif salario < 2000 and tempo < 5:
        return salario * 0.1
    elif salario >= 2000 and tempo >= 5:
        return salario * 0.05
    return 0.0