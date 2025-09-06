Numero_1 = int(input('Digite o 1° Número: \n'))

Numero_2 = int(input('Digite o 2° Número: \n'))

Numero_3 = int(input('Digite o 3° Número: \n'))

if Numero_1 > Numero_2 and Numero_1 > Numero_3:
    print(f'O {Numero_1} é MAIOR!!!')

elif Numero_2 > Numero_1 and Numero_1 > Numero_3:
    print(f'O {Numero_2} é MAIOR!!!')

else :
    print(f'O {Numero_3} é MAIOR!!!')
