'''
Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa
O programa vai perguntar o valor da casa, o salário do comprador e em quantos
anos ele vai pagar

Calcule o valor da prestação mensal,
sabendo que ela não pode exceder 30% do salário
ou então o empréstimo será negado
'''

valor_casa = float(input('Digite o valor da Casa: '))
salarios_comprador = float(input('Qual o Salário do Comprador: '))
anos = int(input('Em quantos a casa vai ser paga: '))

mensalidade = (valor_casa / (anos * 12))
print(f"Valor da casa: {valor_casa:.2f}")
print(f"Prestação: {mensalidade:.2f}")

if mensalidade >= (salarios_comprador * 30 / 100):
    print("Empréstimo negado.")
else:
    print(f'Empréstimo concedido. Mensalidade durante {anos} anos: R${mensalidade:.2f}')
