import random

maquina = random.randint(1, 10)

jogadas = 0

while jogadas < 5:
    jogador = int(input('Tente adivinhar o Número que a Máquina Escolheu (1 á 10): '))
    jogadas += 1

    if jogador == maquina:
        print('Parabêns, Você Acertou o Número!!!')
        break
    else:
        print('Que Pena, Mas Você Errou!!!')

print(f'A Máquina Escolheu o Número: {maquina}')