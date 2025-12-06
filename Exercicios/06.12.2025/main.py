import random


def gerar_numero():
    return random.randint(1,100)


escola_maquina = gerar_numero()


try:

    dificuldade = int(input('1 - Fácil (7 Rodadas)\n'
                            '2 - Médio (5 Rodadas)\n'
                            '3 - Difícil (3 Rodadas)\n'
                            'Digite a Dificuldade: '))

    if 1 <= dificuldade <= 3:

        if dificuldade == 1:
            dificuldade = 7

        elif dificuldade == 2:
            dificuldade = 5

        elif dificuldade == 3:
            dificuldade = 3

    else:
        print(f'Você Digitou {dificuldade}. Que não está entre 1 e 3.')

except ValueError:
    print('Digite uma Entrada Válida!')

contador = 0

dificuldade = dificuldade

while contador < dificuldade:

    try:

        escolha_jogador = int(input(f'Jogada: {contador + 1} de {dificuldade}\n'
                                    'Tente Adivinhar o Numero que a Máquina Escolheu: '))

        if 1 <= escolha_jogador <= 100:

            if escolha_jogador == escola_maquina:
                print('Parabéns. Você Acertou o Numero!')
                break

            elif escolha_jogador > escola_maquina:
                print('Você Chutou um Número Maior!')

            else:
                print('Você Chutou um Número Menor!')

            contador += 1

            if contador == dificuldade:
                print('Que Pena. Acabou as suas Chances!\n'
                      f'O Numero que a Máquina escolheu foi o: {escola_maquina}')
                break

        else:
            print(f'Você Digitou {escolha_jogador}. Que não está entre 1 e 100.')

    except ValueError:
        print('Digite uma Entrada Válida!')
