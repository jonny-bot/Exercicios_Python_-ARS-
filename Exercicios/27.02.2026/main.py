import random

def gerar_numero():
    return random.randint(1, 100)

escolha_maquina = gerar_numero()

try:
    total_tentativas = int(input("Digite o número de tentativas: "))
    contador = 0

    while contador < total_tentativas:
        
        chute = int(input("Digite um número entre 1 e 100: "))

        if 1 <= chute <= 100:

            if chute < escolha_maquina:
                print("O número é maior.")

            elif chute > escolha_maquina:
                print("O número é menor.")

            else:
                print(f"Parabéns! Você acertou o número {escolha_maquina}!")
                break

            contador += 1

            if contador == total_tentativas:
                print(f"Você não acertou o número. O número era {escolha_maquina}.")

        else:
            print("Número inválido. Digite um número entre 1 e 100.")
