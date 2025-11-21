import random


def gerar_numero():
    return random.randint(1,100)


def analisar_numero(numero):
    if numero % 2 == 0:
        print('O Numero é PAR!!!')
    else:
        print('O Numero é IMPAR!!!')


numero_gerado = gerar_numero()

print(f'O Numero Gerado é o: {numero_gerado}')

analisar_numero(numero_gerado)
