def calcular_imc(peso: float, altura: float) -> str:
    imc = peso / (altura * altura)

    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc <= 24.9:
        return "Peso normal"
    elif 25 <= imc <= 29.9:
        return "Sobrepeso"
    elif 30 <= imc <= 34.9:
        return "Obesidade grau I"
    elif 35 <= imc <= 39.9:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"