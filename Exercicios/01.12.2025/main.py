import random


def gerar_numero():
    return random.randint(1,100)


escolha_maquina =gerar_numero()


total_jogadas = int(input('Digite o Total de Jogadas: '))

contador = 0

while contador < total_jogadas:
    while True:
        try:

            escolha_jogador = int(input(f'Rodada: {contador + 1} de {total_jogadas}\n'
                                        'Tente Adivinhar o Numero que a Máquina Escolheu: '))

            if 1 <= escolha_jogador <= 100:

                if escolha_jogador == escolha_maquina:
                    print('Parabéns. Você Acertou!')
                    break

                elif escolha_jogador > escolha_maquina:
                    print('Você Chutou um Numero Maior!')

                else:
                    print('Você Chutou um Numero Menor!')

                contador += 1

                if contador == total_jogadas:
                    print('Que Pena. Acabou as Suas Chances!\n'
                          f'A Maquina Escolheu o Numer: {escolha_maquina}')
                    break

            else:
                print(f'Você Digitou {escolha_jogador}. Que não está entre 1 e 100.')

        except ValueError:
            print('Digite uma Entrada Válida!')
