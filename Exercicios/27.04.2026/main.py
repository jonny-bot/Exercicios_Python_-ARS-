try:

    numero = int(input("Digite um número: "))

    numero_verificado = numero % 2

    if numero_verificado == 0:
        print("O número é par")
    else:        
        print("O número é ímpar")

except ValueError:
    print("Digite uma Entrada Válida")
    