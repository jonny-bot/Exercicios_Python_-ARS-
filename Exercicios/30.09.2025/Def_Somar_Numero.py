def somar_numero_while():
    soma = 0
    while True:
        numero = int(input('Digite um Número: '))
        if numero == 0:
            break
        soma += numero
    print(f'A Soma dos Números deu: {soma}')

somar_numero_while()

def somar_numero_for():
    soma = 0

    print("Digite números para somar. Digite 0 para encerrar.")

    for _ in iter(int, 1):
        numero = int(input("Número: "))
        if numero == 0:
            break
        soma += numero

    print(f"A soma dos números digitados é: {soma}")

somar_numero_for()