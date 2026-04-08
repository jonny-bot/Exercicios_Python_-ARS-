def realizar_deposito(saldo_atual, extrato):

    while True:
        try:

            valor_deposito = float(input('Digite o Valor a ser Depositado: '))

            if valor_deposito <= 0.0:

                print(f'Você Digitou {valor_deposito:.2f}. Você Precisar Digitar um Valor Maior.')

            else:
                saldo_atual += valor_deposito

                extrato.append(f'Deposito: +R${valor_deposito:.2f}')

                print('Deposito Realizado com Sucesso!!!\n'
                      f'Seu Saldo Atual é de: R${saldo_atual:.2f}')

                return saldo_atual

        except ValueError:
            print('Digite uma Entrada Válida!!!')


def realizar_saque(saldo_atual, extrato):

    while True:
        try:

            valor_saque = float(input('Digite o Valor a ser Sacado: '))

            if valor_saque <= 0.0:

                print(f'Você Digitou R${valor_saque:.2f}. Você Precisar Digitar um Valor Maior.')

            elif valor_saque > saldo_atual:

                print('Saldo Insuficiente. Tente Novamente.')

            else:
                saldo_atual -= valor_saque

                extrato.append(f'Saque: -R${valor_saque:.2f}')

                print('Saque Realizado com Sucesso!!!\n'
                      f'Seu Saldo Atual é de: R${saldo_atual:.2f}')

                return saldo_atual
        except ValueError:
            print('Digite uma Entrada Válida!!!')


def realizar_transferencia(saldo_atual, extrato, conta_destino):

    while True:
        try:

            print(f'Seu Saldo Atual: {saldo_atual:.2f}')

            valor_saque = float(input('Digite o Valor a ser Sacado: '))

            if valor_saque <= 0.0:

                print(f'Você Digitou {valor_saque:.2f}. Você Precisar Digitar um Valor Maior.')

            elif valor_saque > saldo_atual:

                print('Saldo Insuficiente. Tente Novamente.')

            else:
                saldo_atual -= valor_saque

                extrato.append(f'Tranferencia {conta_destino}: -R${valor_saque:.2f}')

                print('Tranferencia Realizado com Sucesso!!!\n'
                      f'Seu Saldo Atual é de: R${saldo_atual:.2f}')

                return saldo_atual

        except ValueError:
            print('Digite uma Entrada Válida!!!')


def consultar_estrato(extrato):
    for contagem, lista in enumerate(extrato):
        print(f'{contagem} - {lista}')


def consultar_saldo(saldo_atual):
    print(f'Seu Saldo Atual é de: R${saldo_atual:.2f}')


extrato = []

saldo_atual = float(input('Digite o Saldo Inicial: '))
extrato.append(f'Saldo Inicial: +R${saldo_atual:.2f}')

while True:
    try:

        lista_operacoes = ['Sair da Conta',
                           'Realizar Deposito',
                           'Realizar Saque',
                           'Realizar Tranferencias',
                           'Consultar Extrato',
                           'Consultar Saldo Atual']

        for contador, lista in enumerate(lista_operacoes):
            print(f'{contador} - {lista}')

        escolha_operacao = int(input('Digite uma das operações: '))

        match escolha_operacao:
            case 0:
                print('Fim do Programa...')
                break

            case 1:
                saldo_atual = realizar_deposito(saldo_atual, extrato)

            case 2:
                saldo_atual = realizar_saque(saldo_atual, extrato)

            case 3:
                conta_destino = input('Digite a Conta Destino para ser Depositado: ')
                saldo_atual = realizar_transferencia(saldo_atual, extrato, conta_destino)

            case 4:
                consultar_estrato(extrato)

            case 5:
                consultar_saldo(saldo_atual)

            case _:
                print(f'Você Digitou {escolha_operacao}. Que não está entre 0 e {len(lista_operacoes) - 1}')

    except ValueError:
        print('Digite uma Entrada Válida!!!')
