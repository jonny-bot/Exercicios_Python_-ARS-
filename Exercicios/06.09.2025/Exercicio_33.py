numero_1 = int(input('Informe o primeiro número: '))

numero_2 = int(input('Informe o segundo número: '))

numero_3 = int(input('Informe o terceiro número: '))

maior = numero_1
menor = numero_1

# Maior
if numero_2 > numero_1 and numero_2 > numero_3:
    maior = numero_2

if numero_3 > numero_1 and numero_3 > numero_2:
    maior = numero_3

# Menor
if numero_2 < numero_1 and numero_2 < numero_3:
    menor = numero_2

if numero_3 < numero_1 and numero_3 < numero_2:
    menor = numero_3

print(f'O número {maior} é o MAIOR'.format())

print(f'O número {menor} é o MENOR'.format())