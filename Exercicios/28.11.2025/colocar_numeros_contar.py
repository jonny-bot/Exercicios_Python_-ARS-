lista = []

registro = 0
soma = 0
contagem_registros = 0
while True:
    registro += 1
    contagem_registros += 1
    numero = int(input(f'Digite o {registro}° Número: '))
    if numero != 0:
        lista.append(f'{contagem_registros}° Número: {numero}')
    if numero == 0:
        break
    soma += numero

for i in lista:
    print(f'{i}')

print(f'A soma dos Números deu: {soma}\n'
      f'Você Registrou: {registro - 1} Números.\n')
