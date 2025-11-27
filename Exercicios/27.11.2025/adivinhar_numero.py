import random


def gerar_numero():
    return random.randint(1,100)


escolha_maquina = gerar_numero()


contador_tentativa = 0
total_rodadas = int(input('Digite o Total de Rodadas: '))

while contador_tentativa < total_rodadas:

    while True:
        try:

            escolha_jogador = int(input(f'Rodada: {contador_tentativa + 1} de {total_rodadas}\n'
                                        'Tente Adivinhar o Numero que a Máquina Escolheu: '))

            if 1 <= escolha_jogador <= 100:

                if escolha_jogador == escolha_maquina:
                    print('Parabêns. Você Acertou!')
                    break

                elif escolha_jogador > escolha_maquina:
                    print('O Numero que você chutou é MAIOR!')

                else:
                    print('O Numero que você chutou é MENOR!')

                if 10 <= escolha_maquina <= 30:
                    print('Dica: O número da máquina está entre 10 e 30!')

                elif 31 <= escolha_maquina <= 50:
                    print('Dica: O número da máquina está entre 31 e 50!')

                elif 51 <= escolha_maquina <= 70:
                    print('Dica: O número da máquina está entre 51 e 70!')

                elif 71 <= escolha_maquina <= 90:
                    print('Dica: O número da máquina está entre 71 e 90!')

                contador_tentativa += 1

                if contador_tentativa == total_rodadas:
                    print('Que Pena. Acabou as Suas Chances!\n'
                          f'O Numero que a Máquina Escolheu foi o: {escolha_maquina}')
                    break

            else:
                print(f'Você Digitou: {escolha_jogador}. Que não está entre 1 e 100.')

        except ValueError:
            print('Digite uma Entrada Válida!')
