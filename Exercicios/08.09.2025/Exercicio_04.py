tabuada = int(input('Qual tabuada você Quer: '))

for var in range(1, tabuada + 1):

    if var % 3 == 0 or var % 5 == 0:

        print(f'{tabuada} x {var} = {var}')