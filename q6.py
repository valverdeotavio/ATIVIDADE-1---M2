def verificar_voto(idade: int, nacionalidade: str) -> str:

    if idade < 16:
        return "Não pode votar!"
    elif idade >= 18 and nacionalidade.lower() == "brasileiro":
        return "O voto é obrigatório!"
    return "O voto é opcional."