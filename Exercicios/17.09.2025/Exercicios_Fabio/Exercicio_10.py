import random

random = random.randint(1, 10)

while True:
    numero = int(input('Digite um Número:'))

    if numero == random:
        print('Voce Acertou!!!')
        break
    else:
        print('Voce Errou!!!')