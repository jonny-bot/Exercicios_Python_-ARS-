import random
from time import sleep

escolha = ['Pedra', 'Papel', 'Tesoura']

escolha_maquina = random.choice(escolha)

escolha_jogador = int(input('1 - Pedra, 2 - Papel, 3 - Tesoura\n'
                            'Digite Uma das Opções: '))

if escolha_jogador == 1:
    escolha_jogador = 'Pedra'

elif escolha_jogador == 2:
    escolha_jogador = 'Papel'

elif escolha_jogador == 3:
    escolha_jogador = 'Tesoura'

else:
    print("Opção inválida!")

print('Vamos lá!!!')
for i in range(3, 0, -1):
    sleep(0.5)
    print(i)

print(f"Você escolheu: {escolha_jogador}")

print(f"A máquina escolheu: {escolha_maquina}")

if escolha_jogador == escolha_maquina:
    print('Empate!')

elif (escolha_jogador == 'Pedra' and escolha_maquina == 'Tesoura') or \
     (escolha_jogador == 'Papel' and escolha_maquina == 'Pedra') or \
     (escolha_jogador == 'Tesoura' and escolha_maquina == 'Papel'):

    print('Parabéns, você venceu!')

else:
    print('Você perdeu!')
