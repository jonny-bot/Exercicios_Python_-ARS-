'''
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:

- média abaixo de 5.0: reprovado
- média entre 5.0 e 6,9: recuperação
- média 7.0 ou superior: aprovado
'''

nota1 = float(input('Digite a 1° Nota: '))
nota2 = float(input('Digite a 2° Nota: '))
media = (nota1 + nota2) / 2

if media < 5.0:
    print('O Alunos Está Reprovado!!!')
elif media < 7.0:
    print('O Aluno está de Recuperação!!!')
else:
    print('O Aluno está Aprovado!!!')