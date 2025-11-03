import random


def numero_maquina():
    return random.randint(1, 10)


jogadas = 0
escolha_maquina = numero_maquina()


while jogadas < 5:
    jogadas += 1
    print(f'Você está na {jogadas} de 5')
    escolha_jogador = int(input('Digite Um Número: '))
    if escolha_jogador == escolha_maquina:
        print('Parabêns, Você Acertou!!!')
        break

    elif escolha_jogador != escolha_maquina:
        print('Que Pena, Você Errou!!!')

print(f'A Máquina Escolheu: {escolha_maquina}')