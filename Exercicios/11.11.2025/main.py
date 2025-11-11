valor = float(input('Digite um Valor: '))

cem_reais = int(valor / 100)
valor = valor % 100
print(f'{cem_reais} Notas de R$100,00 Reais.')

sobra = valor

print(f'A sobra é de: {sobra}')