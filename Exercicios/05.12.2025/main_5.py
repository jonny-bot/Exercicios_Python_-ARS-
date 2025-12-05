import random


def gerar_numero():
    return random.randint(1,100)


escolha_maquina = gerar_numero()


contador = 0
total_rodadas = int(input('Digite o Total de Rodadas: '))

while contador < total_rodadas:
    try:

        escolha_jogador = int(input(f'Jogada: {contador + 1} de {total_rodadas}\n'
                                    'Tente Adivinhar o Numero que a Máquina Escolheu: '))

        if 1 <= escolha_jogador <= 100:

            if escolha_jogador == escolha_maquina:
                print('Parabéns. Você Acertou!!!')
                break

            elif escolha_jogador > escolha_maquina:
                print('Você Chutou um Número Maior!')

            else:
                print('Você Chutou um Número Menor!')

            contador += 1

            if contador == total_rodadas:
                print('Que Pena. Acabou as suas Chances!\n'
                      f'A Máquina Escolheu o Numero: {escolha_maquina}')
                break

        else:
            print(f'Você Digitou {escolha_jogador}. Que não está Entre 1 e 100.')

    except ValueError:
        print('Digite uma Entrada Válida!')
