import random

escolha_maquina = random.randint(1,100)

total_tentativas = int(input('Digite o Total de Tentativas: '))

contador = 0

while contador < total_tentativas:

    escolha_jogador = int(input(f'Tentativa: {contador + 1} de {total_tentativas}\n'
                                'Tente Adivinhar o Número que Máquina Escolheu: '))

    if escolha_jogador == escolha_maquina:
        print('Parabêns...Você Acertou!!!')
        break

    elif escolha_jogador > escolha_maquina:
        print('Você Chutou um Número Maior!!!')

    elif escolha_jogador < escolha_maquina:
        print('Você Chutou um Número Menor!!!')

    contador += 1

    if contador == total_tentativas:
        print('Que Pena...Acabou as Suas Tentativas!!!')
        break

print(f'Escolha Máquina: {escolha_maquina}')
