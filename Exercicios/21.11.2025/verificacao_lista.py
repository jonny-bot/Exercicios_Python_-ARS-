def lista():
    lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    return lista


def verificar_numero(numero):
    if numero in lista():
        print('O Número Existe na Lista!!!')
    else:
        print('O Número Não Existe na Lista!!!')


numero = int(input('Digite um Número: '))

verificar_numero(numero)
