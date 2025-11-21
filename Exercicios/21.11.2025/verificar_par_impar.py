import random


def gerar_numero():
    return random.randint(1,10)


numero_gerado = gerar_numero()


antecessor = numero_gerado - 1
sucessor = numero_gerado + 1


print(f'O Número Gerado é o: {numero_gerado}\n'
      f'O Antecessor {antecessor}\n'
      f'O Sucessor {sucessor}.')
