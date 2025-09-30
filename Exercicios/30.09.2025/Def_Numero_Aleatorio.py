def escolha_maquina():

    import random

    random = random.randint(1, 10)
    return random

def escolha_jogador():
    numero_jogador = int(input('Digite um Número: '))
    return numero_jogador

def verificar(escol_maquina, escol_jogador):
    if escol_maquina == escol_jogador:
        print('Você Acertou!!!')
    else:
        print('Você Errou!!!')

maquina = escolha_maquina()
jogador = escolha_jogador()
verificar(maquina, jogador)