soma = 0
num = 0
while True:
    try:
        num += 1
        numero = int(input(f'Digite o {num}° Número: '))
        if numero == 0:
            break
        soma += numero
    except ValueError:
        print(f'Digite uma entrada Válida.')

print(f'A soma dos Números deu: {soma}\n'
      f'Você digitou {num - 1} Números.')