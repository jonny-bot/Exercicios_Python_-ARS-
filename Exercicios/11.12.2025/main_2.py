import random


def gerar_lista(numero):
    lista = []
    return numero.append(lista)


def gerar_numero():
    return random.randint(1, 10)


def contador_numero():
    contador = 1
    total_numeros = int(input('Digite o Total de Números a Ser Gerados: '))
    while contador < total_numeros:
        numero_gerado = gerar_numero()
        gerar_lista(numero_gerado)
