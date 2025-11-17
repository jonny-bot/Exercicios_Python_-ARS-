import random

def gerar_numero():
    return random.randint(1, 100)

numero_maquina = gerar_numero()

contador = 0

jogadas = int(input('Digite o Total de Jogadas: '))

while contador < jogadas:

    while True:
        try:

            numero_jogador = int(input(f'Jogada: {contador + 1} de {jogadas}.\n'
                                       'Tente Adivinhar o Número que Máquina Escolheu: '))

            if 1 <= numero_jogador <= 100:

                if numero_jogador == numero_maquina:
                    print('Parabéns, Você Acertou!!!')
                    break

                elif numero_jogador > numero_maquina:
                    print('Você Errou. O Número que Você Chutou é MAIOR.')

                else:
                    print('Você Errou. O Número que Você Chutou é MENOR.')

                contador += 1

                if contador == jogadas:
                    print('Que Pena. Acabaram as Suas Chances.\n'
                          f'O Número que a Máquina Escolheu eh: {numero_maquina}')
                    break

            else:
                print(f'Você Digitou {numero_jogador}. Que não está entre 1 e 100.')

        except ValueError:
            print('Digite Uma Entrada Válida!!!')