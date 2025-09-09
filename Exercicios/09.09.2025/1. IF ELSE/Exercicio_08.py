print('C - Celsius para Fahrenheit')
print('F - Fahrenheit para Celsius')

Letra = str(input('Digite uma das Opções: ')).lower()

if Letra == 'C':

    C = float(input('Digite o Gráu em Celsius: '))

    F = (C * 1.8) + 32

    print(f'A conversão de Celso para Fahrenheit é {F:.2f}')

else:
     F = float(input('Digite o Gráu em Fahrenheit: '))

     C = (F - 32) * 5 / 9

     print(f'A conversão de Fahrenheit para Celsius é {C:.2f}')