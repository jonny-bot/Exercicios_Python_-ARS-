soma = 0

while True:

    i = int(input('Digite um Número: '))

    if i == 0:
        print('Encerrando...')
        break

    if i % 2 == 0:
        print(i)
        continue
    soma += i
print(f'A soma dos Números deu: {soma}')