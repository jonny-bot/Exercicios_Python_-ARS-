import random


def gerar_numero():
    numero_gerado = random.randint(1,100)
    return numero_gerado


escolha_maquina = gerar_numero()

try:

    total_jogadas = int(input('Digite o Total de Jogadas: '))

    contador = 0

    while contador < total_jogadas:

        escolha_jogador = int(input(f'Jogada: {contador + 1} de {total_jogadas}\n'
                                    'Tente Adivinhar o Número que a Máquina Escolheu (Entre 1 e 100): '))

        if 1 <= escolha_jogador <= 100:

            if escolha_jogador == escolha_maquina:
                print('Parabêns. Você Acertou!!!')
                break

            elif escolha_jogador > escolha_maquina:
                print('Você Chutou Um Número Maior!!!')

            elif escolha_jogador < escolha_maquina:
                print('Você Chutou Um Número Menor!!!')

            contador += 1

            if contador == total_jogadas:
                print('Que Pena. Mas Acabou as Suas Chances!!!\n'
                      f'O Número que Máquina Escolheu foi o: {escolha_maquina}')
                break

        else:
            print(f'Você Digitou {escolha_jogador}. Que não está entre 1 e 100!!!')

except ValueError:
    print('Digite Uma Entrada Válida!!!')
