Numero_1 = int(input('Digite o 1° Número: '))

Numero_2 = int(input('Digite o 2° Número: '))

Numero_3 = int(input('Digite o 3° Número: '))

if Numero_1 > Numero_2 and Numero_1 > Numero_3:
    print(f'O Número {Numero_1} é MAIOR!!!')
elif Numero_2 > Numero_3 and Numero_2 > Numero_1:
    print(f'O Número {Numero_2} é MAIOR!!!')
else:
    print(f'O Número {Numero_3} é MAIOR!!!')