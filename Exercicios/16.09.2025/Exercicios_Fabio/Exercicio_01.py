numero = int(input('Digite um Número: '))

if numero <= 1 and numero % 3 == 0:
    print(f'O {numero} é PAR e é Múltiplo de 3!!!')
else:

        if numero % 5 == 0:
            print(f'O {numero} é Múltiplo de 5')
        else:
            if numero % 2 == 0:
                print(f'O {numero} é Múltiplo de 2')
            elif numero % 3 == 0:
                print(f'O {numero} é Múltiplo de 3')