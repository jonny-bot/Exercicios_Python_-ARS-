def soma():
    soma = 0
    while True:
        numero = int(input('Digite um Número: '))
        if numero == 0:
            break
        soma += numero
    print(f'A soma dos Números deu: {soma}')

soma()