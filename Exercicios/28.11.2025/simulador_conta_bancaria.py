saldo_inicial = float(input('Digite o Inicial: '))

saldo_atual = saldo_inicial

extrato = []

while True:
    try:

        opcao = int(input('0 - Sair do Programa\n'
                          '1 - Fazer Deposito\n'
                          '2 - Fazer Saque\n'
                          '3 - Tirar Extrato\n'
                          'Digite umas das Opções: '))

        if 0 <= opcao <= 3:

            if opcao == 0:
                print('Saindo do Programa...\n'
                      f'Seu Saldo Atual é de: {saldo_atual:.2f}')
                break

            if opcao == 1:
                print(f'Seu Saldo Atual é de: {saldo_atual:.2f}')

                deposito = float(input('Digite o Total a Ser Depositado: '))

                extrato.append('Deposito: ' + str(deposito))

                saldo_atual = saldo_atual + deposito

                print(f'Seu Saldo Atual é de: {saldo_atual:.2f}')

            if opcao == 2:

                print(f'Seu Saldo Atual é de: {saldo_atual:.2f}')

                saque = float(input('Digite o Total a ser Sacado: '))

                if saque > saldo_atual:

                    print('Você não tem Saldo Suficiente!')

                else:

                    saldo_atual = saldo_atual - saque

                    print(f'Você Sacou {saque:.2f}')

                    extrato.append('Saque: ' + str(saque))

                print(f'Seu Saldo Atual é de: {saldo_atual:.2f}')

            if opcao == 3:

                print('=====X EXTRATO X=====')
                for i in extrato:
                    print(i)
                print(f'Seu Saldo Atual é de: {saldo_atual:.2f}\n'
                      f'=====X EXTRATO X=====\n'
                      f'Fim do Programa!')
                break

        else:
            print(f'Você Digitou {opcao}. Que não está Entre 0 e 2.')

    except ValueError:
        print('Digite uma Entrada Válida!')
