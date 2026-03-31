from datetime import datetime

def mostrar_menu():
    lista_opcoes = {0: 'Sair do Programa...',
                    1: 'Realizar Deposito',
                    2: 'Realizar Saque',
                    3: 'Tirar Extrato',
                    4: 'Consultar Saldo Atual'}

    for chave in lista_opcoes:
        print(f'{chave} - {lista_opcoes[chave]}')
    return lista_opcoes


def realizar_deposito(saldo, extrato):
    valor = float(input('Digite o Valor a ser Depositado: '))
    saldo += valor

    agora = datetime.now()
    extrato.append(f'Deposito: {valor:.2f} - {agora.date()}')

    print('Deposito Realizado com Sucesso!!!\n'
          f'Seu Saldo Atual é de: {saldo:.2f}')

    return saldo


def realizar_saque(saldo, extrato):
    valor = float(input('Digite o Valor a ser Sacado: '))

    if valor > saldo:
        print('Valor Insuficiente.')
    else:
        saldo -= valor
        agora = datetime.now()
        extrato.append(f'Saque: {valor:.2f} - {agora.date()}')

        print('Saque Realizado com Sucesso!!!\n'
              f'Seu Saldo Atual é de: {saldo:.2f}')

    return saldo


def mostrar_extrato(extrato, saldo):
    print('=====X EXTRATO X=====')
    for contador, item in enumerate(extrato):
        print(f'{contador + 1}° - {item}')
    print(f'Seu Saldo Atual: {saldo:.2f}')


def consultar_saldo(saldo):
    print(f'Seu Saldo Atual é de: {saldo:.2f}')


def main():
    extrato = []
    saldo = float(input('Digite um Valor Inicial: '))

    while True:
        try:
            lista_opcoes = mostrar_menu()
            opcoes = int(input('Digite Uma das Opções: '))

            if 0 <= opcoes <= (len(lista_opcoes) - 1):

                if opcoes == 0:
                    print('Fim do Programa!!!')
                    break

                elif opcoes == 1:
                    saldo = realizar_deposito(saldo, extrato)

                elif opcoes == 2:
                    saldo = realizar_saque(saldo, extrato)

                elif opcoes == 3:
                    mostrar_extrato(extrato, saldo)

                elif opcoes == 4:
                    consultar_saldo(saldo)

            else:
                print(f'Você Digitou {opcoes} Que não Está Entre 0 e {len(lista_opcoes) - 1}.')

        except ValueError:
            print('Digite uma Entrada Válida!!!')

main()
