def par(numero):
    resultado = numero * 12
    print("Número par:", resultado)

def negativo(numero):
    resultado = numero / 3
    print("Número negativo:", resultado)

def impar(numero):
    resultado = numero ** 2
    print("Número impar:", resultado)

def positivo(numero):
    resultado = numero ** 0.5
    print("Número positivo:", resultado)

def multiplo_de_3(numero):
    resultado = numero / 3
    print("Múltiplo de 3:", resultado)

# numero = int(input("Digite um número: "))

def verifcação(num):

    condicao = False

    if numero % 2 == 0:
        par(numero)
        condicao = True

    if numero < 0:
        negativo(numero)
        condicao = True

    if numero % 2 == 1:
        impar(numero)
        condicao = True

    if numero > 1:
        positivo(numero)
        condicao = True

    if numero % 3 == 0:
        multiplo_de_3(numero)
        condicao = True

    if not condicao:
        print("Nenhuma condição atendida.")

numero = int(input("Digite um número: "))
verifcação(numero)