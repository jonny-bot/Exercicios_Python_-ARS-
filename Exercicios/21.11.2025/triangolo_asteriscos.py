def triangulo_asteriscos():
    for i in range(1, 5 + 1):
        print('*' * i)


def triangulo_asteriscos_invertido():
    for i in range(5, -1, -1):
        print('*' * i)


opcao = int(input('1 - Triangulo Asteriscos\n'
                  '2 - Triangulo Asteriscos Invertidos\n'
                  'Digite uma opção: '))

if opcao == 1:
    triangulo_asteriscos()

elif opcao == 2:
    triangulo_asteriscos_invertido()
