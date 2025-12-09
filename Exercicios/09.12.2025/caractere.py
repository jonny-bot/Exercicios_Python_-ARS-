'''

Caractere: vogal maiúscula
Leia um único caractere.
 Imprima “Vogal maiúscula”,
 “Vogal minúscula”, “Consoante” ou “Outro” (use in com tuplas e isalpha())

'''

def minuscula(nome):
    nome_minuscula = nome.lower()
    print(nome_minuscula)


def maiusculo(nome):
    nome_maiusculo = nome.upper()
    print(nome_maiusculo)


def vogais(nome):
    vogais = "aeiouAEIOU"
    lista_vogais = [letra for letra in nome if letra in vogais]
    print(lista_vogais)


def comprimento(nome):
    comprimento_nome = len(nome)
    print(f'Letras Totais: {(comprimento_nome)}')


try:

    nome = input('Digite Um Nome/Frase: ')

    opcao = int(input('1 - Minuscula\n'
                      '2 - Maiúsculo\n'
                      '3 - Vogais\n'
                      '4 - Comprimento\n'
                      'Digite umas das Opções: '))

    if 1 <= opcao <= 4:

        if opcao == 1:
            minuscula(nome)

        elif opcao == 2:
            vogais(nome)

        elif opcao == 3:
            vogais(nome)

        elif opcao == 4:
            comprimento(nome)

    else:
        print(f'Você Digitou {opcao}. Que não está Entre 1 e 4.')

except ValueError:
    print('Digite uma Entrada Válida!')
