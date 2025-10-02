num = 1
soma = 0
while True:
    numero = int(input(f'Digite o {num}° Número: '))
    num += 1
    if numero == 0:
        break
    soma += numero
j = (num - 2)
print(f'A Soma deu: {soma}')
if j == 1:
    print(f'Você Digitou {j} Número.')
else:
    print(f'Você Digitou {j} Número(s).')
