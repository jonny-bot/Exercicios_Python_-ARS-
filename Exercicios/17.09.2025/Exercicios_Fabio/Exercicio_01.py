'''

Múltiplos e paridade
Leia um inteiro n. Diga se ele é par e múltiplo de 3; se é par ou múltiplo de 5; e se não é múltiplo de 2 nem de 3.

'''

numero = int(input('Digite um Número: '))

if numero % 2 == 0 and numero % 3 == 0:
    print(f'O {numero} é PAR e é Múltiplo de 3!!!')
else:

        if numero % 2 == 0 and numero % 5 == 0:
            print(f'O {numero} é Múltiplo de 5')
        else:

            if numero % 2 != 0 and numero % 3 != 0:
                print(f"O {numero} não é múltiplo de 2 nem de 3.")