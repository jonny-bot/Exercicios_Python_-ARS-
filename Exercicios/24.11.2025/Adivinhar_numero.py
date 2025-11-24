import random


lista = []


def gerar_numero():
    return random.randint(1, 10)


def jogatina():

    contador = 0
    pontos = 0
    total_de_jogadas = int(input('Digite o total de Jogadas: '))

    while contador < total_de_jogadas:

        escolha_maquina = gerar_numero()

        try:
            escolha_jogador = int(input(f'Rodada: {contador+1} de {total_de_jogadas}\n'
                                        'Tente Adivinhar o Número que a Máquina Escolheu: '))

            if escolha_jogador == escolha_maquina:
                print('Parabéns. Você Acertou!!!')
                pontos += 10
                temp = str(escolha_maquina)
                lista.append(temp)

            elif escolha_jogador > escolha_maquina:
                print('Você Chutou um Número Alto!!!')
                temp = str(escolha_maquina)
                lista.append(temp)

            else:
                print('Você Chutou um Número Baixo!!!')
                temp = str(escolha_maquina)
                lista.append(temp)

            contador += 1
            print(f"Pontuação atual: {pontos}")

        except ValueError:
            print('Digite Uma Entrada Válida!!!')

    print(f"Fim do jogo! Você fez {pontos} ponto(s).")

    contador_numero = 0
    for i in lista:
        contador_numero += 1
        print(f'O {contador_numero}° Numero que a Máquina Escolheu: {i}')

jogatina()
