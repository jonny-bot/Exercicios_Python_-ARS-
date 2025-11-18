def lista():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def analisar_numero(numero):
    if numero in lista():
        print('É Verdadeiro!!!')
        return True
    else:
        print('É Falso!!!')
        return False

numero = int(input('Digite um Número: '))

analisar_numero(numero)
