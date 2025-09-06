numero = int(input('Digite o Numero: \n'))

resultado = 1

for i in range(1, numero + 1):
    resultado *= i
    print(resultado)