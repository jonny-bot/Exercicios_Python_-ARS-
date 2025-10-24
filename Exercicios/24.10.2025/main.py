import random

escolha_maquina = random.randint(1,100)

rodadas = int(input("Vamos ter quantas rodadas: "))
chances = 1

while chances <= rodadas:
    escolha_jogador = int(input(f"Tente Adivinhar Qual o Número Que a Máquina Escolheu {chances} de {rodadas - chances}: "))
    if escolha_jogador == escolha_maquina:
        print('Parabêns, Você Acertou!!!')
        break

    else:
        if escolha_jogador > escolha_maquina:
            print('Você Digitou um Número Maior!!!')
            chances += 1

        if escolha_jogador < escolha_maquina:
            print('Você Digitou um Número Menor!!!')
            chances += 1

if chances >= rodadas:
    print('Que pena, Acabou as Suas Chances!!!')

print(f'A Máquina escolheu o Número: {escolha_maquina}')