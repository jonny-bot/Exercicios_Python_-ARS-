def par(numero):
    if numero % 2 == 0:
        resultado = numero * 12
        return resultado

def negativo(numero):
    if numero <= -1:
        resultado = numero / 3
        return resultado

def impar(numero):
    if numero % 2 == 1:
        resultado = numero ** 2
        return resultado

def positivo(numero):
    if numero > 0:
        resultado = numero ** 0.5
        return resultado

def multiplo_de_3(numero):
    if numero % 3 == 0:
        resultado = numero / 3
        return resultado

'''
def f(numero):
    if numero % 2 == 0:
        par(numero)

    elif numero <= -1:
        negativo(numero)

    elif numero % 2 == 1:
        impar(numero)

    elif numero > 0:
        positivo(numero)

    elif numero % 3 == 0:
        multiplo_de_3(numero)
'''

numero = int(input('Digite um Número: '))


print(par(numero))
print(negativo(numero))
print(impar(numero))
print(positivo(numero))
print(multiplo_de_3(numero))


def verificador(num):



    return resul