import random

numero_maquina = random.randint(1, 10)

rodadas = 0

jogadas = 0

print('Fácil - 7 Chances || Médio - 5 Chances || Dificil - 3 Chances')

while True:
    try:
        dificuldade = int(input('Digite: (1 - Fácil || 2 - Médio || 3 - Difícil):'))
        if dificuldade not in (1, 2, 3):
            print('Escolha inválida. Digite 1, 2 ou 3.')
            continue
        if dificuldade == 1:
            jogadas = 7
        elif dificuldade == 2:
            jogadas = 5
        elif dificuldade == 3:
            jogadas = 3
        break
    except ValueError:
        print('Digite uma entrada válida (número inteiro).')

while rodadas < jogadas:
    rodadas += 1
    numero_jogador = int(input(f"Tente adivinhar o Número que Máquina escolheu entre 1 a 10 ({rodadas} de {jogadas}): "))

    if numero_jogador < numero_maquina:
        print('O Número da Máquina é MAIOR!!!')

    if numero_jogador > numero_maquina:
        print('O Número da Máquina é MENOR!!!')

    if numero_jogador == numero_maquina:
        print('Parabêns, Você Acetou o Número!!!')
        break

    if rodadas == jogadas:
        print('Que Pena, Acabou as suas Chances!!!')
        break

print(f"A máquina escolheu: {numero_maquina}")