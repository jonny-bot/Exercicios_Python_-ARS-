def escolha_maquina():
    import random

    lista = ['Pedra', 'Papel', 'Tesoura']
    maquina = random.choice(lista)
    return maquina

def escolha_jogador():
    jogador = input('Digite um Número: ').lower()
    return jogador

def verificar(escol_maquina, escol_jogador):
    if escol_jogador == 'pedra' and escol_maquina == 'tesoura':
        print('O jogador ganhou!!!')

    elif escol_jogador == 'tesoura' and escol_maquina == 'papel':
        print('O jogador ganhou!!!')

    elif escol_jogador == 'papel' and escol_maquina == 'pedra':
        print('O jogador ganhou!!!')

    else:
        print('A Máquina ganhou!!!')

maquina = escolha_maquina()
jogador = escolha_jogador()
verificar(maquina, jogador)