def data_valida(dia: int, mes: int, ano: int) -> bool:
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if(ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        dias_por_mes[1] = 29

    if ano > 0 and 1 <= mes <= 12 and 1 <= dia <= dias_por_mes[mes-1]:
        return True
    return False