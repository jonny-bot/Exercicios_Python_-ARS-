def somar_numeros():
    
    soma = 0

    while True:

        numero = int(input("Digite um número: "))

        if numero == 0:
            print('Fim do Programa')
            break

        soma += numero
        
    print(f'A Soma dos Números é: {soma}')


def gerar_lista():

    lista = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]

    soma = sum(lista) / len(lista)

    print(f'A Média dos Números é: {soma}')

gerar_lista()
