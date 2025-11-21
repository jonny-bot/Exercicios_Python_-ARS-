def celsius_fahrenheit(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    print(celsius)
    return celsius


def fahrenheit_celsius(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    print(fahrenheit)
    return fahrenheit

while True:
    try:

        opcoes = int(input('0 - Sair do Programa || 1 - celsius para fahrenheit || 2 - fahrenheit para celsius\n'
                           'Digite umas das Opções: '))

        if opcoes == 0:
            print('Sair do Programa!!!')
            break

        elif opcoes == 1:
            fahrenheit = float(input('Digite os Graús em fahrenheit: '))
            celsius_fahrenheit(fahrenheit)

        elif opcoes == 2:
            celsius = float(input('Digite os Graús em celsius: '))
            fahrenheit_celsius(celsius)

        else:
            print(f'Você Digitou {opcoes}. Que não está entre 0 e 2.')

    except ValueError:
        print('Digite uma Entrada Válida!!!')
