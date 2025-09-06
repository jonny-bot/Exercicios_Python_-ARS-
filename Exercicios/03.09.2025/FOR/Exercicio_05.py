# Fatorial com for: calcule n! usando 'for'

numero = int(input('Qual o numero primo você quer: '))

fatorial = 1

for var in range(1, numero + 1):
    fatorial *= var

print(fatorial)
