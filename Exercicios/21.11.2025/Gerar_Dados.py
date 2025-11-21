import random


lista_dados = []


def tipos_dados(dado):
    #  D4, D6, D8, D10, D12 e D20

    return random.randint(1, dado)


contador = 1

total_dados = int(input('Digite quantos dados vamos gerar: '))

while contador < total_dados:

    while True:
        try:

            escolha_dado = int(input(f'Você Gerou {contador} de {total_dados} Dados.\n'
                                     '0 - Sair do Programa\n'
                                     '1 - D4\n'
                                     '2 - D6\n'
                                     '3 - D8\n'
                                     '4 - D10\n'
                                     '5 - D12\n'
                                     '6 - D20\n'
                                     'Digite qual Dado Você Quer: '))

            if escolha_dado not in (0, 1, 2, 3, 4, 5, 6):
                print(f'Você Digitou {escolha_dado}. Que não está entre 0 e 6.')

            if escolha_dado == 0:
                print('Fim do Programa!!!')
                break

            if contador == total_dados:
                print('Já Gerei Todos os Dados!!!')
                break

            if escolha_dado == 1:

                dado = 4

                numero_dado = tipos_dados(dado)

                temp = 'Dado: ' + str(numero_dado)

                print(f'O Dado Caiu no: {numero_dado}')

                lista_dados.append(temp)

                contador += 1

            if escolha_dado == 2:

                dado = 6

                numero_dado = tipos_dados(dado)

                temp = 'Dado: ' + str(numero_dado)

                print(f'O Dado Caiu no: {numero_dado}')

                lista_dados.append(temp)

                contador += 1

            if escolha_dado == 3:

                dado = 8

                numero_dado = tipos_dados(dado)

                temp = 'Dado: ' + str(numero_dado)

                print(f'O Dado Caiu no: {numero_dado}')

                lista_dados.append(temp)

                contador += 1

            if escolha_dado == 4:

                dado = 10

                numero_dado = tipos_dados(dado)

                temp = 'Dado: ' + str(numero_dado)

                print(f'O Dado Caiu no: {numero_dado}')

                lista_dados.append(temp)

                contador += 1

            if escolha_dado == 5:

                dado = 10

                numero_dado = tipos_dados(dado)

                temp = 'Dado: ' + str(numero_dado)

                print(f'O Dado Caiu no: {numero_dado}')

                lista_dados.append(temp)

                contador += 1

            if escolha_dado == 6:

                dado = 20

                numero_dado = tipos_dados(dado)

                temp = 'Dado: ' + str(numero_dado)

                print(f'O Dado Caiu no: {numero_dado}')

                lista_dados.append(temp)

                contador += 1

        except ValueError:
            print('Digite Uma Entrada Válida!!!')

contador_dados = 1
print(f'Você Gerou {total_dados}')
for i in lista_dados:
    print(f'{contador_dados}° Dado: {i}')
    contador_dados += 1