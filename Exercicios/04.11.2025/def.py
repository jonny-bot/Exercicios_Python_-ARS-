def verificar_numero(numero):
    #  Verificar se o Número Existe na Lista
    lista = [1, 2, 3 , 4]

    if numero in lista:
        print('É Verdadeiro!!!')
        return True
    else:
        print('É Falso!!!')
        return False

numero = int(input('Digite Um Número: '))
verificar_numero(numero)