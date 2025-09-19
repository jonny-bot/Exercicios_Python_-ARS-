'''

Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento.

'''

# salários até R$ 280,00 (incluindo) : aumento de 20%

def reajuste_20(salario):
    percentual = 0.20
    if salario <= 280:
        reajuste = salario + (salario * percentual)
        print(f'O Salario antes do reajuste era de: R${salario}')
        print(f'O Percentual de aumento é de:       {percentual}%')
        print(f'O Valor de aumento é de:            R${reajuste - salario:.2f}')
        print(f'O Novo salário com reajusto é de:   RS{reajuste}')

# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%

def reajuste_15(salario):
    percentual = 0.15
    if salario >= 281 and salario <= 700:
        reajuste = salario + (salario * percentual)
        print(f'O Salario antes do reajuste era de: R${salario}')
        print(f'O Percentual de aumento é de:       {percentual}%')
        print(f'O Valor de aumento é de:            R${reajuste - salario:.2f}')
        print(f'O Novo salário com reajusto é de:   RS{reajuste}')

# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%

def reajuste_10(salario):
    percentual = 0.10
    if salario >= 701 and salario <= 1500:
        reajuste = salario + (salario * percentual)
        print(f'O Salario antes do reajuste era de: R${salario}')
        print(f'O Percentual de aumento é de:       {percentual}%')
        print(f'O Valor de aumento é de:            R${reajuste - salario:.2f}')
        print(f'O Novo salário com reajusto é de:   RS{reajuste}')

# salários de R$ 1500,00 em diante : aumento de 5%

def reajuste_05(salario):
    percentual = 0.05
    if salario >= 1501:
        reajuste = salario + (salario * percentual)
        print(f'O Salario antes do reajuste era de: R${salario}')
        print(f'O Percentual de aumento é de:       {percentual}%')
        print(f'O Valor de aumento é de:            R${reajuste - salario:.2f}')
        print(f'O Novo salário com reajusto é de:   RS{reajuste}')

def verificar(sal):

    verificar_salario = False

    if salario <= 280:
        verificar_numero = True
        reajuste_20(salario)

    if salario <= 700:
        verificar_numero = True
        reajuste_15(salario)

    if salario <= 1500:
        verificar_numero = True
        reajuste_10(salario)

    if salario >= 1501:
        verificar_numero = True
        reajuste_05(salario)

salario = float(input('Digite o Sálario: R$'))
verificar(salario)