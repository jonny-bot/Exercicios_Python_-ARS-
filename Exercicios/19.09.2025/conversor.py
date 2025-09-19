import random


def valor_maquina():
    maquina = random.randint(1, 100)
    return maquina


def chute_jogador():
    valor = 0
    while valor < 1 or valor > 100:
        valor = int(input("Digite um valor entre 1 e 100: "))
    return valor


def comparar_com_maquina(maquina, chute):
    if maquina == chute:
        print(f"A máquina escolheu {maquina} e você ACERTOU!\n")

        return True
    elif maquina > chute:
        print(f"A máquina escolheu um valor maior.\n")
        return False
    elif maquina < chute:
        print(f"A máquina escolheu um valor menor.\n")
        return False


def jogadas(tentativas):
    tentativas += 1
    return tentativas


print("Qual jogo que jogar?")
print("1 - Adivinhar número.")
print("2 - Sair.")
print("")
jogo = int(input("Digite o número do jogo: "))
print("")

while True:
    if jogo == 1:
        maquina = valor_maquina()
        chute = 0
        rodada = 0
        while chute != maquina:
            print(f"Tentativa {rodada+1}")
            chute = chute_jogador()
            rodada = jogadas(rodada)
            if comparar_com_maquina(maquina, chute):
                break
            if rodada == 5:
                print("Acabou as 5 tentativas")
                print(f"O valor da máquina era {maquina}")
                print("GAME OVER!")
                break

    if jogo == 2:
        break
