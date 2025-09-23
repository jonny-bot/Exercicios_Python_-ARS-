import random
from time import sleep

lista = ['pedra', 'papel', 'tesoura']

maquina = random.choice(lista)

jogador = input('Escolha entre, Pedra, Papel e Tesoura: ').lower()

for i in range(3, 0, -1):
    sleep(0.5)
    print(f'O jogo vai começar em: {i}')

if jogador == maquina:
    print(f'A Máquina escolheu {maquina} e o jogador escolheu {jogador}. DEU EMPATE!!!')

elif (jogador == 'pedra' and maquina == 'tesoura') or (jogador == 'papel' and maquina == 'pedra') or (jogador == 'tesoura' and maquina == 'papel'):
    print(f'A Máquina escolheu {maquina} e o jogador escolheu {jogador}. O JOGADOR GANHOU!!!')

else:
    print(f'A Máquina escolheu {maquina} e o jogador escolheu {jogador}. A MÁQUINA GANHOU!!!')