# Faça um programa que pede dois inteiro e armazene em duas variáveis.
# Em seguida, troque o valor das variáveis e exiba na tela

variavel_1 = int(input('Digite o 1° Número: '))
variavel_2 = int(input('Digite o 2° Número: '))

variavel_1,variavel_2 = variavel_2, variavel_1

print(variavel_1)
print(variavel_2)