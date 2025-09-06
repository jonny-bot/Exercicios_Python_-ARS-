lado_1 = float(input('Digite o 1° Lado: \n'))

lado_2 = float(input('Digite o 2° Lado: \n'))

lado_3 = float(input('Digite o 3° Lado: \n'))

if lado_1 + lado_2 > lado_3 and lado_1 + lado_3 > lado_2 and lado_2 + lado_3 > lado_1:
    print('É um Triangulo!!!')
else:
    print('Não é um Triangulo!!!')

if lado_1 == lado_2 == lado_3:
    print('O Triangulo é Equilátero!!!')

elif (lado_1 == lado_2 > lado_3 or lado_1 == lado_3 > lado_2) or (lado_2 == lado_3 > lado_1 or lado_2 == lado_1 > lado_3) and lado_3 == lado_1 > lado_2 and lado_3 == lado_2 > lado_1:
    print('O Triangulo é Isósceles!!!')
else:
    print('O Triangulo é Escaleno!!!')