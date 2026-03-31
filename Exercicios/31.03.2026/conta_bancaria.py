from datetime import datetime

extrato = []

saldo_inicial = float(input('Digite um Valor Inicial: '))
saldo_atual = saldo_inicial

while True:
    try:

        lista_opcoes = {0:'Sair',
                        1:'Realizar Deposito',
                        2:'Realizar Saque',
                        3:'Tirar Extrato',
                        4:'Consultar Saldo Atual'}

        for lista in lista_opcoes:
            print(f'{lista} - {lista_opcoes[lista]}')

        opcoes = int(input('Digite Uma das Opções: '))

        if 0 <= opcoes <= (len(lista_opcoes) - 1):

            if opcoes == 0:
                print('Fim do Programa!!!')
                break

            elif opcoes == 1:
                valor = float(input('Digite o Valor a ser Depositado: '))

                saldo_atual += valor

                agora = datetime.now()

                extrato.append(f'Deposito: {valor:.2f} - {agora.date()}')

                print('Deposito Realizado com Sucesso!!!\n'
                      f'Seu Saldo Atual é de: {saldo_atual:.2f}')

            elif opcoes == 2:
                valor = float(input('Digite o Valor a ser Sacado: '))

                if valor > saldo_atual:

                    print('Valor Insuficiente.')

                else:
                    saldo_atual -= valor

                    agora = datetime.now()

                    extrato.append(f'Saque: {valor:.2f} - {agora.date()}')

                    print('Saque Realizado com Sucesso!!!\n'
                          f'Seu Saldo Atual é de: {saldo_atual:.2f}')

            elif opcoes == 3:
                print('=====X EXTRATO X=====')
                for contador, i in enumerate(extrato):
                    print(f'{contador + 1}° - {i}')
                print(f'Seu Saldo Atual: {saldo_atual}')

            elif opcoes == 4:
                print(f'Seu Saldo Atual é de: {saldo_atual:.2f}')

        else:
            print(f'Você Digitou {opcoes} Que não Está Entre 0 e {len(lista_opcoes) - 1}.')

    except ValueError:
        print('Digite uma Entrada Válida!!!')
