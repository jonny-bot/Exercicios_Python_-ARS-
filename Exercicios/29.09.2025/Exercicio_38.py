'''
Escreva um programa que leia dois números inteiros e compare-os,
mostrando na tela uma mensagem:
- o primeiro valor é maior
- o segundo valor é maior
- não existe valor maior; os dois são iguais
'''

numero1 = int(input('Digite o 1° valor: '))

numero2 = int(input('Digite o 2° valor: '))

if numero1 > numero2:
    print(f'O Número {numero1} é Maior que o Número {numero2}.')

elif numero2 > numero1:
    print(f'O Número {numero2} é Maior que o Número{numero1}.')

else:
    print(f'Não existe valor maior. Os números são iguais.')