import q1, q2, q3, q4, q5, q6, q7, q8, q9, q10
from utils import input_float, input_int

def main():
    while True:
        print("\n=== MENU M1 ===")
        print("1 - Questão 1 (Bônus Funcionário)")
        print("2 - Questão 2 (Classificação Triângulo)")
        print("3 - Questão 3 (IMC)")
        print("4 - Questão 4 (Notas e Aprovação)")
        print("5 - Questão 5 (Data Válida)")
        print("6 - Questão 6 (Voto Obrigatório ou Opcional)")
        print("7 - Questão 7 (Risco Financeiro)")
        print("8 - Questão 8 (Sequência de Pontuação)")
        print("9 - Questão 9 (Preço com Desconto VIP)")
        print("10 - Questão 10 (Validação de Senha)")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            salario = input_float("Digite o salário: ")
            tempo = input_int("Digite o tempo de empresa (anos): ")
            print("Bônus:", q1.calcular_bonus(salario, tempo))

        elif opcao == "2":
            lado1 = input_float("Digite o lado 1: ")
            lado2 = input_float("Digite o lado 2: ")
            lado3 = input_float("Digite o lado 3: ")
            print("Tipo:", q2.classificar_triangulo(lado1, lado2, lado3))

        elif opcao == "3":
            peso = input_float("Digite o peso (kg): ")
            altura = input_float("Digite a altura (m): ")
            print("Classificação IMC:", q3.calcular_imc(peso, altura))

        elif opcao == "4":
            notas = []
            for i in range(3):
                notas.append(input_float(f"Digite a nota {i+1}: "))
            print(q4.avaliar_notas(notas))

        elif opcao == "5":
            dia = input_int("Digite o dia: ")
            mes = input_int("Digite o mês: ")
            ano = input_int("Digite o ano: ")
            if q5.data_valida(dia, mes, ano):
                print("Data válida ")
            else:
                print("Data inválida ")

        elif opcao == "6":
            idade = input_int("Digite a idade: ")
            nacionalidade = input("Digite a nacionalidade: ")
            print(q6.verificar_voto(idade, nacionalidade))

        elif opcao == "7":
            idade = input_int("Digite a idade: ")
            renda = input_float("Digite a renda mensal: ")
            dividas = input_float("Digite o valor das dívidas: ")
            print("Risco:", q7.analisar_risco(idade, renda, dividas))

        elif opcao == "8":
            entrada = input("Digite a sequência (4 letras A, B, C ou D): ")
            print("Pontuação:", q8.sequence(entrada))

        elif opcao == "9":
            preco = input_float("Digite o preço do produto: ")
            vip = input("É cliente VIP? (s/n): ").lower() == "s"
            print("Preço final:", q9.calcular_preco_final(preco, vip))

        elif opcao == "10":
            senha = input("Digite a senha: ")
            if q10.validar_senha(senha):
                print("Senha válida ")
            else:
                print("Senha inválida ")

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
