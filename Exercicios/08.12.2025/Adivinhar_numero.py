import random


def gerar_numero():
    return random.randint(1,100)


def escolher_dificuldade(dificuldade):
    try:

        if 1 <= dificuldade <= 3:

            mapa = {1: 7, 2: 5, 3: 3}

            dificuldade = mapa[dificuldade]

            print(f"Dificuldade ajustada para {dificuldade}")

        else:
            print(f"Você digitou {dificuldade}, que não está entre 1 e 3.")

    except ValueError:
        print("Digite uma entrada válida!")

    return dificuldade


escolha_maquina = gerar_numero()


dificuldade = int(input('1 - Fácil (7 Rodadas) || 2 - Médio (5 Rodadas) || 3 - Difícil (3 Rodadas)\n'
                            'Escolha a Dificúldade: '))


dificuldade = escolher_dificuldade(dificuldade)


contador = 0
total_rodadas = dificuldade

while contador < total_rodadas:

    try:

        escolha_jogador = int(input(f'Rodada: {contador + 1} de {total_rodadas}\n'
                                    'Tente adivinhar o Numero que a Máquina Escolheu: '))

        if 1 <= escolha_jogador <= 100:

            if escolha_jogador == escolha_maquina:
                print('Parabêns. Você Acertou!!!')
                break

            elif escolha_jogador > escolha_maquina:
                print('Você Chutou um Número Maior!')

            else:
                print('Você Chutou um Número Menor!')

            if escolha_maquina <= 10:
                print('O Número está Entre 1 e 10')

            if 11 <= escolha_maquina <= 30:
                print('O Número está Entre 11 e 30.')

            if 31 <= escolha_maquina <= 50:
                print('O Número está Entre 31 e 50.')

            if 51 <= escolha_maquina <= 70:
                print('O Número está Entre 51 e 70.')

            if 71 <= escolha_maquina <= 90:
                print('O Número está Entre 71 e 90.')

            if escolha_maquina >= 91:
                print('O Número é Maior que 91')

            contador += 1

            if contador == total_rodadas:
                print('Que Pena. Acabou as Suas Chances!\n'
                      f'O Número que a Máquina Escolheu foi o: {escolha_maquina}')
                break

        else:
            print(f'Você Digitou {escolha_jogador}. Que não está entre 1 e 100.')

    except ValueError:
        print('Digite umas Entrada Válida!')
