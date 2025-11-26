valor = float(input('Digite o valor: '))

cem_reais = int(valor / 100)
valor = valor % 100
print(f'{cem_reais} de Notas de R$100,00.')

cinquenta_reais = int(valor / 50)
valor = valor % 50
print(f'{cinquenta_reais} de Notas de R$50,00.')

vinte_reais = int(valor / 20)
valor = valor % 20
print(f'{vinte_reais} de Notas de R$20,00.')

dez_reais = int(valor / 10)
valor = valor % 10
print(f'{dez_reais} de Notas de R$10,00.')

cinco_reais = int(valor / 5)
valor = valor % 5
print(f'{cinco_reais} de Notas de R$5,00.')

sobra = valor

print(f'A Sobra deu: {sobra}')