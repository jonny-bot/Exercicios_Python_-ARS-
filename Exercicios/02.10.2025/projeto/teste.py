num = 1
soma = 0
while True:
    numero = int(input(f'Digite o {num}° Número: '))
    num += 1
    if numero == 0:
        break
    soma += numero
print(f'A Soma deu: {soma}\n'
      f'Você Digitou {num - 2} Número(s).')
