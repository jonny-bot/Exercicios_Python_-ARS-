def par(numero):
    if numero % 2 == 0:
        resultado = numero * 12
        print(f'O Número escolhido é o {numero} e ele é PAR!!! E o resultado é: {resultado}')

def negativo(numero):
    if numero <= -1:
        resultado = numero / 3
        print(f'O Número escolhido é o {numero} e ele é NEGATIVO!!! E o resultado é: {resultado}')

def impar(numero):
    if numero % 2 == 1:
        resultado = numero ** 2
        print(f'O Número escolhido é o {numero} e ele é IMPAR!!! E o resultado é: {resultado}')

def positivo(numero):
    if numero >= 1:
        resultado = numero ** 0.5
        print(f'O Número escolhido é o {numero} e ele é POSITIVO!!! E o resultado é: {resultado}')

def multiplo_de_3(numero):
    if numero % 3 == 0:
        resultado = numero / 3
        print(f'O Número escolhido é o {numero} e ele é MULTIPLO DE 3 !!! E o resultado é: {resultado}')

def verificar(num):

    verificar_numero = False

    if num % 2 == 0:
        verificar_numero = True
        par(numero)

    if num <= -1:
        verificar_numero = True
        par(numero)

    if num % 2 == 1:
        verificar_numero = True
        impar(numero)

    if numero >= 1:
        verificar_numero = True
        positivo(numero)

    if numero % 3 == 0:
        verificar_numero = True
        multiplo_de_3(numero)

numero = int(input('Digite um Número: '))
verificar(numero)