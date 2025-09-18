import random

random = random.randint(1, 10)

total_rodadas = int(input('Vamos ter quantas Rodadas: '))

rodadas = 0

while True:

    jogador = int(input('Digite um Número: '))

    if random == jogador:
        print('Você Acertou!!!')
        break

    else:
        print(f'Você Errou!!! Você ainda tem {rodadas + 1} de {total_rodadas}')
        rodadas += 1

        if rodadas == total_rodadas:
            print('Você perdeu as suas chances')
            break

print(f'A Máquina escolheu: {random}')