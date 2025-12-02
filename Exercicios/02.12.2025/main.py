valor_inicial = float(input('Digite o Valor Inicial: '))

saldo_atual = valor_inicial

while True:
    try:

        opcao = int(input('0 - Sair do Programa...\n'
                          '1 - Fazer Deposito\n'
                          '2 - Fazer Saque\n'
                          '3 - Consultar Saldo\n'
                          'Digite uma das Opção: '))

        if 0 <= opcao <= 3:

            if opcao == 0:
                print('Saindo do Programa\n'
                      f'Seu Saldo Final foi de: {saldo_atual}')
                break

            elif opcao == 1:

                print(f'Seu Saldo Atual é de: R${saldo_atual:.2f}')

                deposito = float(input('Digite o Valor a ser Depositado: '))

                saldo_atual = saldo_atual + deposito

                print(f'Você Depositou: R${deposito:.2f}\n'
                      f'Seu Saldo Atual é de: R${saldo_atual:.2f}')

            elif opcao == 2:

                print(f'Seu Saldo Atual é de: R${saldo_atual:.2f}')

                saque = float(input('Digite o Valor a ser Sacado: '))

                if saque > saldo_atual:
                    print('Você não tem Saldo Suficiente.')

                else:

                    saldo_atual = saldo_atual - saque

                    print(f'Você Sacou: R${saque:.2f}\n'
                          f'Seu Saldo Atual é de: R${saldo_atual:.2f}')

            elif opcao == 2:
                print(f'Seu Saldo Atual é de: R${saldo_atual:.2f}')

        else:
            print(f'Você Digitou {opcao}. Que não entre 0 e 2.')

    except ValueError:
        print('Digite uma Entrada Válida!')
