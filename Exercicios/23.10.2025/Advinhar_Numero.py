import random

escolha_maquina = random.randint(1,100)

jogadas = 1

tentativas = int(input('Vamos ter Quantas Tentativas: '))

while jogadas <= tentativas:
    try:
        escolha_jogador = int(input('Tente Adivinhar o Número que a Máquina Escolheu: '))
        if escolha_jogador < 1 or escolha_jogador > 100:
            print('Digite um Número Inteiro Válido!!!')
        else:
            if escolha_jogador == escolha_maquina:
                print('Parabéns, Você Acertou!!!')
                break
            elif escolha_jogador < escolha_maquina:
                print('O Número que você colocou é Menor!!!\n'
                      f'Você tem {jogadas} de {tentativas - jogadas}')
                jogadas += 1
            elif escolha_jogador > escolha_maquina:
                print('O Número que você colocou é Maior!!!\n'
                      f'Você tem {jogadas} de {tentativas - jogadas}')
                jogadas += 1
    except ValueError:
        print('Digite uma Entrada Válida!!!')

if jogadas > tentativas:
    print('Que Pena, Acabou as Suas Chances!!!')