print('Para converter de  Celsius ---> Fahrenheit Digite C ou c')
print('Para converter de  Fahrenheit ---> Celsius Digite F ou f')

letra = (input('Digite uma letra: \n')).lower()

if letra == 'c':
    C = float(input('Digite a temperatura em Celsios: \n'))
    F = (C * 1.8) + 32
    print(f'A temperatura em Fahrenheit é de {F}')

elif letra == 'f':
        F = float(input('Digite a temperatura em Fahrenheit: \n'))
        C = (F * 32) * (5 / 9)
        print(f'A temperatura em Celsios é de {C}')

else:
    print('Opção Inválida!!!')