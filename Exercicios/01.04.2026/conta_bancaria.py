import random
import string
from datetime import datetime


def gerar_token():
    # Escolhe 4 letras aleatórias
    letras = ''.join(random.choice(string.ascii_uppercase) for _ in range(4))

    # Escolhe 4 números aleatórios
    numeros = ''.join(random.choice(string.digits) for _ in range(4))

    # Junta letras e números e embaralha
    codigo = letras + numeros
    codigo = ''.join(random.sample(codigo, len(codigo)))
    
    return codigo


def criacao_menu():
    lista_opcao = ['Sair do Programa',
                   'Realizar Deposito',
                   'Realizar Saque',
                   'Consultar Extrato',
                   'Consultar Saldo Atual']

    for contador, lista in enumerate(lista_opcao):
        print(f'{contador} - {lista}')

    return lista_opcao


def realizar_deposito(saldo, extrato):
    valor = float(input('Digite o Total a ser Depositado: '))
    saldo += valor

    data_atual = datetime.now()

    token = gerar_token()

    extrato.append(f'Valor: {valor:.2f} || Data: {data_atual.date()} || Token: {token}')

    print(f'Deposito Realizado com Sucesso!!!\n'
          f'Seu Saldo Atual é de: {saldo:.2f}')

    return saldo


def realizar_saque(saldo, extrato):
    valor = float(input('Digite o Valor a Ser Sacado: '))

    if valor > saldo:
        print('Saldo Insuficiente!!!')
    else:
        saldo -= valor

        data_atual = datetime.now()

        token = gerar_token()

        extrato.append(f'Valor: {valor:.2f} || Data: {data_atual.date()} || Token: {token}')

        print(f'Saque Realizado com Sucesso!!!\n'
              f'Seu Saldo Atual é de: {saldo:.2f}')

    return saldo


def consultar_extrato(saldo, extrato):
    print('=====X EXTRATO X=====')
    for contador, lista_extrato in enumerate(extrato):
        print(f'{contador} - {lista_extrato}')
    print(f'Seu Saldo Atual é de: {saldo:.2f}')


def consultar_saldo(saldo):
    print(f'Seu Saldo Atual de: {saldo:.2f}')


def main():
    extrato = []
    saldo = float(input('Digite o Saldo Inicial: '))

    while True:
        try:

            exibir_menu = criacao_menu()
            escolha_opcao = int(input('Digite uma das Opções: '))

            match escolha_opcao:

                case 0:
                    print('Programa Finalizado...')
                    break

                case 1:
                    saldo = realizar_deposito(saldo, extrato)

                case 2:
                    saldo = realizar_saque(saldo, extrato)

                case 3:
                    consultar_extrato(saldo, extrato)

                case 4:
                    consultar_saldo(saldo)

                case _:
                    print(f'Você Digitou {escolha_opcao}. Que não está entre 0 e {len(exibir_menu) - 1}')

        except ValueError:
            print('Digite Uma Entrada Válida!!!')

if __name__ == '__main__':
    main()
