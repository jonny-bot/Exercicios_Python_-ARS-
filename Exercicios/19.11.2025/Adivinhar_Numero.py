import random


def gerar_numero():
    numero = random.randint(1,100)
    return numero


def adivinhar_numero():
    escolha_maquina = gerar_numero()

    contador = 0

    total_jogadas = int(input('Digite o Total de Jogadas: '))

    while contador < total_jogadas:

        while True:
            try:

                escolha_jogador = int(input('Tente Adivinhar o Número que a Máquina escolheu.\n'
                                            f'{contador + 1} de {total_jogadas}: '))

                if 1 <= escolha_jogador <= 100:

                    if escolha_jogador == escolha_maquina:
                        print('Parabêns. Você Acertou!!!')
                        break

                    elif escolha_jogador > escolha_maquina:
                        print('Você Chutou um Número Muito Alto!!!')

                    else:
                        print('Você Chutou um Número Muito Baixo!!!')

                    contador += 1

                    if contador == total_jogadas:
                        print('Que Pena. Mas Acabou as suas Chances!!!\n'
                              f'A Máquina Escolheu o Número: {escolha_maquina}')
                        break

                else:
                    print(f'Você Digitou {escolha_jogador}. Que não está entre 1 e 100.')

            except ValueError:
                print('Digite uma Entrada Válida!!!')

adivinhar_numero()
