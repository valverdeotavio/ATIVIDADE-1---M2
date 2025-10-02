def input_float(mensagem: str) -> float:
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Valor inválido. Por favor, insira um número válido.")

def input_int(mensagem: str) -> int:
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Valor inválido. Por favor, insira um número inteiro válido.")