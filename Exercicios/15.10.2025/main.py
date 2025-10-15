'''
soma = 0
num = 0
lista = []
while True:
    try:
        num += 1
        numero = int(input(f'Digite o {num}° Número: '))
        if numero == 0:
            break
        soma += numero
        lista.append(numero)
    except ValueError:
        print('Entrada inválida. Por favor, digite um número inteiro.')
print(f'A soma dos números deu: {soma}\n'
      f'Você digitou {num - 1} Números.')

contagem = 1
for i in lista:
    print(f'{contagem}° Número:{i}')
    contagem += 1
'''

import random

n = int(input("Quantos números aleatórios você quer gerar? "))

numeros_aleatorios = []

for _ in range(n):
    numero = random.randint(1, 1000)
    numeros_aleatorios.append(numero)

contagem = 1
for i in numeros_aleatorios:
    print(f'{contagem}° Número: {i}')
    contagem += 1
