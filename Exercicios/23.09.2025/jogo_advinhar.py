import random

maquina = random.randint(1, 10)

tentativas = 1

while tentativas <= 2:

    jogador = 0

    print(f'Tentativa {tentativas} de 2')

    while jogador < 1 or jogador > 10:
        jogador = int(input('Digite um Número de 1 à 10: '))
    tentativas += 1

    if jogador == maquina:
        print('Parabêns Você Acertou!!!')
        break

    elif jogador < maquina:
        print('A Máquina Escolheu um Número Maior!!!')

    elif jogador > maquina:
        print('A Máquina Escolheu um Número Menor!!!')

print(f'A Máquina escolheu: {maquina}')