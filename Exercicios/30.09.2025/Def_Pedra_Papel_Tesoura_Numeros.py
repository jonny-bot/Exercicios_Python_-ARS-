def escolha_maquina():
    import random
    maquina = random.randint(1, 3)
    print(f'A Máquina escolheu: {maquina}')
    return maquina


def escolha_jogador():
    print('1. Pedra \n2. Papel \n3. Tesoura')
    jogado = int(input('Digite a sua escolha: '))
    print(f'O Jogador escolheu: {jogado}')
    return jogado


def jogada(player, computador):

    if player == computador:
        print('Deu Empate!!!')

    if player == 1 and computador == 3:
        print('O Jogador colocou 1. Pedra, e Máquina colocou 3. Tesoura. O JOGADOR ganhou.')

    if player == 1 and computador == 2:
        print('O Jogador colocou 1. Pedra, e Máquina colocou 2. Papel. A MAQUINA ganhou.')

    if player == 2 and computador == 1:
        print('O Jogador colocou 2. Papel, e Máquina colocou 1. Pedra. O JOGADOR ganhou.')

    if player == 2 and computador == 3:
        print('O Jogador colocou 2. Papel, e Máquina colocou 3. Tesoura. A MAQUINA ganhou.')

    if player == 3 and computador == 1:
        print('O Jogador colocou 3. Tesoura, e Máquina colocou 1. Pedra. O JOGADOR ganhou.')

    if player == 3 and computador == 2:
        print('O Jogador colocou 3. Tesoura, e Máquina colocou 2. Papel. A MAQUINA ganhou.')

jogador = escolha_jogador()
pc = escolha_maquina()
jogada(jogador, pc)