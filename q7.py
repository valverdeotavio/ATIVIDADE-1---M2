def analisar_risco(idade: int, renda: float, dividas: float) -> str:
    if renda > 0:
        perc_divida = (dividas / renda) * 100
    else:
        perc_divida = 100

    if renda < 2000 and perc_divida > 50:
        return "Alto"
    elif (2000 <= renda <= 5000) or (30 <= perc_divida <= 50):
        return "Medio"
    elif renda > 5000 and perc_divida < 30:
        return "Baixo"
    else:
        return "Médio-Baixo"