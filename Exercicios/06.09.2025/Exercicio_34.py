salario = float(input('Informe seu salário: R$'))

if salario <= 1250.00:
    aumento = salario + (salario * 15 / 100)

else:
    aumento = salario + (salario * 10 / 100)

print(f'O salário com aumento é: R$ {aumento:.2f}'.format())