# Jogo da adivinhação
import random


def gerar_numero():
    return random.randint(1, 100)


escolha_maquina = gerar_numero()


contador = 0
total_jogadas = int(input('Digite o total de Jogas: '))

while contador < total_jogadas:

    while True:
        try:

            escolha_jogador = int(input(f'Jogada: {contador + 1} de {total_jogadas}\n'
                                        'Tente Adivinhar o Número que a Máquina Escolheu: '))

            if 1 <= escolha_jogador <= 100:

                if escolha_jogador == escolha_maquina:
                    print('Parabéns. Você Acertou o Número.')
                    break

                elif escolha_jogador > escolha_maquina:
                    print('O Número que Você Chutou é MAIOR!!!')

                else:
                    print('O Número que você Chutou é MENOR!!!')

                contador += 1

                if contador == total_jogadas:
                    print('Que Pena. Acabou as Suas Chances!!!\n'
                          f'O Número que a Máquina Escolheu é: {escolha_maquina}')
                    break

            else:
                print(f'Você Digitou {escolha_jogador}. Que não está entre 1 e 100.')

        except ValueError:
            print('Digite umas Entrada Válida!!!')
