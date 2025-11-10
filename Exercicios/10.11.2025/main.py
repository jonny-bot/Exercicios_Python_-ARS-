valor = float(input('Digite um Valor: '))

cem_reais = int(valor / 100)
valor = valor % 100
print(f'{cem_reais} Notas de R$100,00 Reais.')

cinquenta_reais = int(valor / 50)
valor = valor % 50
print(f'{cinquenta_reais} Notas de R$50,00 Reais.')

vinte_reais = int(valor / 20)
valor = valor % 20
print(f'{vinte_reais} Notas de R$20,00 Reais.')

dez_reais = int(valor / 10)
valor = valor % 10
print(f'{dez_reais} Notas de R$10,00 Reais.')

cinto_reais = int(valor / 5)
valor = valor % 5
print(f'{cinto_reais} Notas de R$5,00 Reais.')

sobra = valor

print(f'Sobra: {sobra}')