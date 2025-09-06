from random import randint

maquina = randint(0, 5)

chute = int(input('Adivinhe o número um número entre 0 e 5: '))

if chute == maquina:
    print('Você ACERTOU!!!')

else:
    print('Você ERROU!!!')

    print(f'O número era {maquina}'.format())