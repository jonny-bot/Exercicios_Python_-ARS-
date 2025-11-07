valor = float(input('Digite um Valor: '))

cem_reais = int(valor / 100)
valor = valor % 100
print(f'{cem_reais}')

cinquenta_reais = int(valor / 50)
valor = valor % 50
print(f'{cinquenta_reais}')

sobra = valor

print(f'A sobre foi de: {sobra}')