soma = 0
while True:
    numero = int(input('Digite Um Número: '))
    if numero == 0:
        break
    soma += numero
print(f'A soma dos Números deu: {soma}')