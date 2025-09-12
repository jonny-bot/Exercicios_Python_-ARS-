def par(numero):
    if numero % 2 == 0:
        resultado = numero * 12
        print(f"Número par. Resultado:", resultado)

def negativo(numero):
    if numero <= -1:
        resultado = numero / 3
        print(f"Número negativo. Resultado:", resultado)

def impar(numero):
    if numero % 2 == 1:
        resultado = numero ** 2
        print(f"Número ímpar. Resultado:", resultado)

def positivo(numero):
    if numero >= 1:
        resultado = numero ** 0.5
        print(f"Número positivo. Resultado:", resultado)

def multiplo_de_3(numero):
    if numero % 3 == 0:
        resultado = numero / 3
        print(f"Múltiplo de 3. Resultado:", resultado)

def verificação(num):
    condicoes_atingidas = False

    if num % 2 == 0:
        par(num)
        condicoes_atingidas = True

    if num <= -1:
        negativo(num)
        condicoes_atingidas = True

    if num % 2 == 1:
        impar(num)
        condicoes_atingidas = True

    if num >= 1:
        positivo(num)
        condicoes_atingidas = True

    if num % 3 == 0:
        multiplo_de_3(num)
        condicoes_atingidas = True

    if not condicoes_atingidas:
        print("Nenhuma condição atendida.")

numero = int(input("Digite um número: "))
verificação(numero)
