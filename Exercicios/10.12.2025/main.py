saldo_inicial = float(input('Digite o Valor Inicial: '))

saldo_atual = saldo_inicial


while True:
    try:

        opcoes = int(input('0 - Sair || 1 - Deposito || 2 - Saque || 3 - Consultar Saldo\n'
                           'Digite uma das Opções: '))

        if opcoes <= 4:

            if opcoes == 0:
                print('Fim do Programa...')
                break

            elif opcoes == 1:

                deposito = float(input(f'Seu Saldo Atual é de: R${saldo_atual:.2f}\n'
                                       'Digite o Total a ser Depositado: '))

                saldo_atual = saldo_atual + deposito

                print(f'Você Depositou: {deposito}\n'
                      f'Seu Saldo Atual é de: R${saldo_atual:.2f}')

            elif opcoes == 2:

                saque = float(input(f'Seu Saldo Atual é de: R${saldo_atual:.2f}\n'
                                       'Digite o Total a ser Depositado: '))

                if saque > saldo_atual:
                    print('Você não tem Saldo Suficiênte.\n'
                          f'Seu Saldo Atual é de: R${saldo_atual:.2f}')

                else:

                    saldo_atual = saldo_atual - saque

                    print(f'Você Depositou: {saque}\n'
                          f'Seu Saldo Atual é de: R${saldo_atual:.2f}')

            elif opcoes == 3:
                print(f'Seu Saldo Atual é de: R${saldo_atual:.2f}')

        else:
            print(f'Você Digitou {opcoes}. Que não está Entre 0 e 3.')

    except ValueError:
        print('Digite uma Entrada Válida!')
