def validar_senha(senha: str) -> bool:
    return (
        len(senha) >= 8
        and any(c.isupper() for c in senha)
        and any(c.islower() for c in senha)
        and any(c.isdigit() for c in senha)
        and any(c in "!@#$%" for c in senha)
    )