from time import sleep

def escolha_maquina():
    import random

    lista = ['pedra', 'papel', 'tesoura']
    maquina = random.choice(lista)
    return maquina

def escolha_jogador():
    jogador = input('Escolha entre: \nPedra - Papel - Tesoura: ').lower()
    return jogador

def verificacao(escol_jogador, escol_maquina):
    if escol_jogador == 'pedra' and escol_maquina == 'tesoura':
        print(f'O Jogador escolheu {escol_jogador}. \n'
              f'A Máquina escolheu {escol_maquina}. \n'
              f'O Jogador GANHOU!!!')

    elif escol_jogador == 'tesoura' and escol_maquina == 'papel':
        print(f'O Jogador escolheu {escol_jogador}. \n'
              f'A Máquina escolheu {escol_maquina}. \n'
              f'O Jogador GANHOU!!!')

    elif escol_jogador == 'papel' and escol_maquina == 'pedra':
        print(f'O Jogador escolheu {escol_jogador}. \n'
              f'A Máquina escolheu {escol_maquina}. \n'
              f'O Jogador GANHOU!!!')

    elif escol_jogador == 'tesoura' and escol_maquina == 'papel':
        print(f'O Jogador escolheu {escol_jogador}. \n'
              f'A Máquina escolheu {escol_maquina}. \n'
              f'O Jogador GANHOU!!!')

    else:
        print(f'O Jogador escolheu {escol_jogador}. \n'
              f'A Máquina escolheu {escol_maquina}. \n'
              f'A Máquina GANHOU!!!')

maquina = escolha_maquina()
jogador = escolha_jogador()
verificacao(maquina,jogador)