import random


def gerar_numero():
    return random.randint(1,100)


escolha_maquina = gerar_numero()

contador = 0
total_rodadas = int(input('Digite o Total de Rodadas: '))

while contador < total_rodadas:
    try:

        escolha_jogador = int(input(f'Jogada: {contador + 1} de {total_rodadas}\n'
                                    'Tente Adivinhar o Número que a Máquina Escolheu: '))

        if 1 <= escolha_jogador <= 100:

            if escolha_jogador == escolha_maquina:
                print('Parabêns. Você Acertou!')
                break

            elif escolha_jogador > escolha_maquina:
                print('Você Chutou um Número Maior!')

            else:
                print('Você Chutou um Número Menor!')

            # Dica
            if escolha_maquina < 10:
                print('O Número escolhido se encontra menor que 10.')

            if 10 <= escolha_maquina <= 29:
                print('O Número escolhido se encontra entre 10 e 29.')

            if 30 <= escolha_maquina <= 49:
                print('O Número escolhido se encontra entre 30 e 49.')

            if 50 <= escolha_maquina <= 79:
                print('O Número escolhido se encontra entre 50 e 79.')

            if escolha_maquina >= 80:
                print('O Número escolhido se encontra Maior que 80.')

            contador += 1

            if contador == total_rodadas:
                print('Que Pena. Acabou as suas Chances!\n'
                      f'O Número que a Máquina Escolheu foi o: {escolha_maquina}')
                break

        else:
            print(f'Você Digitou {escolha_jogador}. Que não está Entre 1 e 100.')

    except ValueError:
        print('Digite uma Entrada Válida!')

print('O Número que a Máquina Escolheu foi o: {')
