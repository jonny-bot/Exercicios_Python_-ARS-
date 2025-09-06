'''

Problema: Faça um algoritmo que leia o preço de um produto e
          mostre seu novo preço, com 5% de desconto.

'''

produto = float(input('Digite o preço do produto: R$'))

desconto = float(input('Digite o desconto: '))

total = produto - (produto * desconto / 100)

print(f'O preço do produto com desconto fica {total}')