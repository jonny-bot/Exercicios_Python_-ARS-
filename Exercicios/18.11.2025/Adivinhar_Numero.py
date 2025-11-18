import random


def gerar_numero():
    return random.randint(1, 100)


numero_maquina = gerar_numero()

contador = 0

total_jogadas = int(input('Digite o Total de Jogadas: '))

while contador < total_jogadas:

    while True:

        try:

            numero_jogador = int(input(f'Tente Adivinhar o Número que a Máquina Escolheu'
                                       f'(jogada: {contador + 1} de {total_jogadas}): '))

            if 1 <= numero_jogador <= 100:

                if numero_jogador == numero_maquina:
                    print('Parabêns, Você Acertou!!!')
                    break

                elif numero_jogador > numero_maquina:
                    print('O Número que Você Chutou é Maior!!!')

                else:
                    print('O Número que Você Chutou é Menor!!!')

                contador += 1

                if contador == total_jogadas:
                    print('Que Pena. Acabou as suas Chances!!!\n'
                          f'O Número que a máquina Escolheu foi o: {numero_maquina}')
                    break

            else:
                print(f'Você Digitou {numero_jogador}. Que não está entre 1 e 100.')

        except ValueError:
            print('Digite uma Entrada Válida!!!')
