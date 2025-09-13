'''

Labirinto Numerico

Você esta preso em um labirinto representando por uma matriz (lista de listas).
Seu objetivo é sair do labirinto, partindo de uma posição inicial e chegando ate´a saida.
O jogador pode se mover ara cima, baixo, esquerdo ou direita, mas não pode
    atravesar paredes (paredes são presensentadas pelo numero1)
Caminho livre é 0, inicio é 2 e saida é 3.

'''

def mostrar_labirinto(labirinto, pos):
    for i, linha in enumerate(labirinto):
        for j, valor in enumerate(linha):
            if (i, j) == pos:
                print('P', end='')  # P = Player
            elif valor == 1:
                print('#', end='')  # Parede
            elif valor == 0:
                print('.', end='')  # Caminho livre
            elif valor == 2:
                print('S', end='')  # Início
            elif valor == 3:
                print('E', end='')  # Saída
        print()  # Nova linha após cada linha do labirinto


def encontrar_inicio(labirinto):
    for i in range(len(labirinto)):
        for j in range(len(labirinto[0])):
            if labirinto[i][j] == 2:
                return (i, j)
    return None


def mover(pos, direcao, labirinto):
    linhas = len(labirinto)
    colunas = len(labirinto[0])
    i, j = pos

    direcoes = {
        'cima': (i - 1, j),
        'baixo': (i + 1, j),
        'esquerda': (i, j - 1),
        'direita': (i, j + 1)
    }

    if direcao not in direcoes:
        print("Movimento inválido. Use cima, baixo, esquerda ou direita.")
        return pos, False

    novo_i, novo_j = direcoes[direcao]

    if 0 <= novo_i < linhas and 0 <= novo_j < colunas:
        if labirinto[novo_i][novo_j] != 1:
            return (novo_i, novo_j), True
        else:
            print("Bateu na parede! Escolha outro caminho.")
            return pos, False
    else:
        print("Fora do labirinto! Escolha outro caminho.")
        return pos, False


def main():
    labirinto = [
        [1, 1, 1, 1, 1],
        [1, 2, 0, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 3, 1],
        [1, 1, 1, 1, 1],
    ]

    pos = encontrar_inicio(labirinto)

    print("🧠 Bem-vindo ao Labirinto Numérico!")
    print("Movimente-se usando: cima, baixo, esquerda, direita")
    print("Seu objetivo é chegar no 'E' (saída)!\n")

    while True:
        mostrar_labirinto(labirinto, pos)
        direcao = input("Para onde deseja ir? (cima/baixo/esquerda/direita): ").strip().lower()
        nova_pos, andou = mover(pos, direcao, labirinto)

        if andou:
            pos = nova_pos
            if labirinto[pos[0]][pos[1]] == 3:
                mostrar_labirinto(labirinto, pos)
                print("🎉 Parabéns! Você saiu do labirinto!")
                break


if __name__ == '__main__':
    main()
