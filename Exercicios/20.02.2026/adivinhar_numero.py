import random


def gerar_numero():
    numero_gerado = random.randint(1,100)
    return numero_gerado


def numero_jogador():
    try:

        numero = int(input('Tente Adivinhar o Número que Máquina Escolheu (Entre 1 e 100): '))

        match numero:
            case n if 1 <= n <= 100:
                print(f'Você digitou {n}, que está dentro do intervalo válido!')

            case _:
                print(f'Você digitou {numero}, que não está entre 1 e 100.')

    except ValueError:
        print('Digite Uma Entrada Válida!!!')


def escolha_dificuldade():
    rodadas = int(input('1 - Fácil (7 Rodadas) | 2 - Médio (5 Rodadas) | 3 - Difícil (3 Rodadas)\n'
                        'Escolha a Dificuldade: '))

    match rodadas:
        case 1:
            return 7

        case 2:
            return 5

        case 3:
            return 3

        case _:
            print(f'Você Digitou: {rodadas}. Que não está entre 1 e 3.')
            return None


escolha_maquina = gerar_numero()

dificuldade = escolha_dificuldade()

jogador = numero_jogador()
