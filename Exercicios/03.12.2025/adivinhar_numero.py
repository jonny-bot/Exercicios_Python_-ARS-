import random


def gerar_numero():
    return random.randint(1, 100)


escolha_maquina = gerar_numero()

contador = 0
total_jogadas = int(input('Digite o Total de Jogadas: '))

while contador < total_jogadas:

    while True:
        try:

            escolha_jogador = int(input(f'Jogada: {contador + 1} de {total_jogadas}\n'
                                        'Tente Adivinhar o Número que a Máquina Escolheu: '))

            if 1 <= escolha_jogador <= 100:

                if escolha_jogador == escolha_maquina:
                    print('Parabéns. Você Acertou!!!')
                    break

                elif escolha_jogador > escolha_maquina:
                    print('Você Chutou um Número Maior!!!')

                else:
                    print('Você Chutou um Número Menor!!!')

                contador += 1

                if contador == total_jogadas:
                    print('Acabou as suas Chances.\n'
                          f'A Máquina Escolheu o Número: {escolha_maquina}')
                    break

            else:
                print(f'Você Digitou {escolha_jogador}. Que não está entre 1 e 100.')

        except ValueError:
            print('Digite uma Entrada Válida!')
