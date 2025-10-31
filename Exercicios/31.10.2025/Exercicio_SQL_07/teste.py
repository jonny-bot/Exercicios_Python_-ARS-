import random

def competicao_computadores():
    def numero_computador_1():
        return random.randint(1, 100)

    def numero_computador_2():
        return random.randint(1, 100)

    computador_1 = numero_computador_1()
    computador_2 = numero_computador_2()

    if computador_1 > computador_2:
        print('O Computador 1 Ganhou!!!')

    elif computador_1 < computador_2:
        print('O Computador 2 Ganhou!!!')

    elif computador_1 == computador_2:
        print('Deu Empate!!!')

    print(f'Número Escolhido Pelo Computador 1: {computador_1}')

    print(f'Número Escolhido Pelo Computador 2: {computador_2}')

def gerar_numero(numero):
    return random.randint(1, numero)

opcao = int(input('Digite uma Opçao (1 - Competição de Computadores || 2 - Outro): '))
if opcao == 1:
    competicao_computadores()
if opcao == 2:
    numero = int(input('Digite um Número: '))
    numero_gerado = gerar_numero(numero)
    print(f'O Número Gerado foi o: {numero_gerado}')