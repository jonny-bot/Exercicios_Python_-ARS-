saldo_inicial = float(input('Digite o Saldo Inicial: '))

saldo_atual = saldo_inicial

while True:
    try:

        opcao = int(input('0 - Sair do Programa\n'
                          '1 - Fazer Deposito\n'
                          '2 - Fazer Saque\n'
                          '3 - Consultar Saldo\n'
                          'Digite umas das Opções: '))

        if opcao == 0:
            print('Saindo do Programa...')
            break

        elif opcao == 1:

            print(f'Seu Saldo Atual é de: R${saldo_atual:.2f}')

            deposito = float(input('Digite o Total a ser Depositado: '))

            saldo_atual = saldo_inicial + deposito

            print(f'Deposito Realizado com Sucesso\n'
                  f'\n'
                  f'Voçê Depositou R${deposito:.2f}.\n'
                  f'Seu Novo Saldo é de: R${saldo_atual:.2f}')

        elif opcao == 2:

            print(f'Seu Saldo Atual é de: R${saldo_atual:.2f}')

            saque = float(input('Digite o Total a ser Depositado: '))

            if saque > saldo_atual:

                print('Você não tem saldo o Suficiente...\n'
                      f'Seu Saldo Atual é de: R${saldo_atual:.2f}')

            else:

                saldo_atual = saldo_inicial - saque

                print(f'Saque Realizado com Sucesso\n'
                      f'\n'
                      f'Voçê Depositou R${saque:.2f}.\n'
                      f'Seu Novo Saldo é de: R${saldo_atual:.2f}')

        elif opcao == 3:

            print(f'Seu Saldo Atual é de: R${saldo_atual:.2f}')

    except ValueError:
        print('Digite Uma Entrada Válida!')
