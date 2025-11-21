def maior_numero(numero_1, numero_2, numero_3):

    if numero_1 > numero_2 and numero_1 > numero_3:
        print(f'O Numero {numero_1} é Maior!!!\n'
              f'E ele foi o 1° Numero a ser Digitado.')

    elif numero_2 > numero_1 and numero_2 > numero_3:
        print(f'O Numero {numero_2} é Maior!!!\n'
              f'E ele foi o 2° Numero a ser Digitado.')

    elif numero_3 > numero_1 and numero_3 > numero_2:
        print(f'O Numero {numero_3} é Maior!!!\n'
              f'E ele foi o 3° Numero a ser Digitado.')


def numeros_digitados():
    numero_1 = int(input('Digite o 1° Numero: '))
    numero_2 = int(input('Digite o 2° Numero: '))
    numero_3 = int(input('Digite o 3° Numero: '))

    maior_numero(numero_1, numero_2, numero_3)

numeros_digitados()