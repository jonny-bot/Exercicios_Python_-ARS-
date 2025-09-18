'''

Calculadora de reajuste salarial Peça o salário atual e aplique:
15% de aumento se for até R$ 1.000
10% se for entre R$ 1.001 e R$ 2.000
5% se for acima de R$ 2.000

'''

salario_atual = int(input('Digite o Salário: R$'))

if salario_atual <= 1000:
    percentual = 1.15

elif 1001 >= salario_atual <= 2000:
    percentual = 1.10

else:
    percentual = 1.05

novo_salario = salario_atual * percentual

print(f'O novo salário com reajuste é de: R$ {novo_salario}')