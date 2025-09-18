'''

Calculadora de reajuste salarial Peça o salário atual e aplique:
15% de aumento se for até R$ 1.000
10% se for entre R$ 1.001 e R$ 2.000
5% se for acima de R$ 2.000

'''

def reajuste_15(salario):
    if salario <= 1000:
        novo_salario = salario + (salario * 0.15)
        print(f'O Novo Salário com reajuste é de: R${novo_salario:.2f}')

def reajuste_10(salario):
    if salario >= 1001 and salario <= 2000:
        novo_salario = salario + (salario * 0.10)
        print(f'O Novo Salário com reajuste é de: R${novo_salario:.2f}')

def reajuste_05(salario):
    if salario > 2000:
        novo_salario = salario + (salario * 0.05)
        print(f'O Novo Salário com reajuste é de: R${novo_salario:.2f}')

def verificar(sal):

    if sal <= 1000:
        reajuste_15(sal)

    elif sal >= 1001 and sal <= 2000:
        reajuste_10(sal)

    elif sal > 2000:
        reajuste_05(sal)

    else:
        print("Valor inválido.")

salario = float(input('Qual o seu Salário: '))
verificar(salario)
