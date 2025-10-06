import random

numero_maquina = random.randint(1, 100)

total_jogadas = int(input(f"1 - Fácil (7 Rodadas) | 2 - Médio (5 Rodadas) | 3 - Difícil (3 Rodadas)\n"
                          f"Escolha a Dificuldade: "))

rodadas = 1

if total_jogadas == 1:
    total_jogadas = 7

if total_jogadas == 2:
    total_jogadas = 5

if total_jogadas == 3:
    total_jogadas = 3

while True:
    try:
        entrada = int(input(f"Digite um número entre 1 e 100 (Jogada {rodadas} de {total_jogadas}): "))
        if rodadas == total_jogadas:
            print('Que pena, acabou suas chances\n'
                  f'A Máquina escolheu o: {numero_maquina}')
            break
        if entrada == numero_maquina:
            print("Parabéns! Você acertou o número.")
            break
        elif entrada < numero_maquina:
            print("Número incorreto. O número da máquina é MAIOR.")
            rodadas += 1
        else:
            print("Número incorreto. O número da máquina é MENOR.")
            rodadas += 1
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")