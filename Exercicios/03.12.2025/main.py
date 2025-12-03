import random


def gerar_numero():
    return random.randint(1000,9999)


numero_gerado = gerar_numero()


print(f'O Número Gerado pela Máquina foi o: {numero_gerado}')
