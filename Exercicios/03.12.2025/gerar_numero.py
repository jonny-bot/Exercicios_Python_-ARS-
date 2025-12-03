import random


def gerar_numero():
    return random.randint(1, 100)


lista = []


contador_registros = 0

total_registos = 10

while contador_registros < total_registos:

    numero_gerado = gerar_numero()

    lista.append(numero_gerado)

    contador_registros += 1

print(f'Números gerados: {lista}')

print(f'Maior número: {max(lista)}')

print(f'Menor número: {min(lista)}')
