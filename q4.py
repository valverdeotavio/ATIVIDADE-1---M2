from typing import List

def avaliar_notas(notas: List[float]) -> str:
    if any(nota <= 0 for nota in notas):
        return "Reprovação automática por nota zero!"
    
    media = sum(notas) / len(notas)

    if media >= 7:
        return "Aprovado!"
    elif media >= 5:
        return "Recuperação!"
    else:
        return "Reprovado!"