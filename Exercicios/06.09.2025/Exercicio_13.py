''''

Problema: Faça um algoritmo que leia o salário de um funcionário
          e mostre seu novo salário, com 15% de aumento.

'''

salario = float(input('Digite o seu salário: R$'))

porcentagem = float(input('Qual o seu reajuste: '))

reajuste = salario + (salario * porcentagem / 100)

print(f'Seu salário com o reajuste fica em {reajuste}')