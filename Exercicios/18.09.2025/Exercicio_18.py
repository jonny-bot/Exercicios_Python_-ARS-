import random
from time import sleep

opcoes = ['pedra', 'papel', 'tesoura']

while True:

    computador = random.choice(opcoes)

    jogador = input("Escolha pedra, papel ou tesoura: ").lower()

    for i in reversed(range(1, 4)):
        print(f'O Jogo vai se iniciar em: {i}')
        sleep(1)

    if jogador == computador:
        print("Empate!")

    elif (jogador == 'pedra' and computador == 'tesoura') or \
         (jogador == 'papel' and computador == 'pedra') or \
         (jogador == 'tesoura' and computador == 'papel'):
        print("Você ganhou!")
        break

    else:
        print("Computador ganhou!")
        continue

print(f"Computador escolheu: {computador}")