from xml.dom.minidom import ProcessingInstruction

Numero1 = float(input('Digite o 1° Número: \n'))

Numero2 = float(input('Digite o 2° Número: \n'))

print('Digite um Operador Mais (+) , Menos (-) , Vezes (*) , Dividir (/)')

operadores = input('Operador: \n').lower()

if operadores == '+':
    total = Numero1 + Numero2
    print(f'A soma dos {Numero1} + {Numero2} é de: {total}')

elif operadores == '-':
        total = Numero1 - Numero2
        print(f'A subtração dos {Numero1} - {Numero2} é de: {total}')

elif operadores == '*':
    total = Numero1 * Numero2
    print(f'A multiplicação dos {Numero1} * {Numero2} é de: {total}')

elif operadores == '/':
    if Numero2 == 0:
        print('Números divisivos por 0')
    else:
        total = Numero1 / Numero2
        print(f'A multiplicação dos {Numero1} / {Numero2} é de: {total}')

else:
    print('Operador Invalido!!!')