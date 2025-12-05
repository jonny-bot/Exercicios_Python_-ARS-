
saldo_inicial = float(input('Digite o Saldo Inicial: '))

saldo_atual = saldo_inicial

while True:
    try:

        opcao = int(input('0 - Sair do Programa\n'
                          '1 - Fazer Deposito\n'
                          '2 - Fazer Saques\n'
                          '3 - Verificar Saldo Atual\n'
                          'Digite umas das Opções: '))

        if opcao <= 0 or opcao <= 3: # if 0 <= opcao <= 3:

            if opcao == 0:
                print('Fim do Programa...\n'
                      f'Seu Saldo ao Final do Programa é de: R${saldo_atual:.2f}')
                break

            elif opcao == 1:

                print(f'Seu Saldo Atual é de: R${saldo_atual:.2f}')

                deposito = float(input('Digite o Total a Ser Depositado: '))

                saldo_atual = saldo_atual + deposito

                print(f'Você Depositou: R${deposito:.2f}\n'
                      f'Seu Saldo Atual é de: R${saldo_atual:.2f}')

            elif opcao == 2:

                print(f'Seu Saldo Atual é de: R${saldo_atual:.2f}')

                saque = float(input('Digite o Total a Ser Sacado: '))

                if saque > saldo_atual:

                    print('Você não tem Saldo Suficiente...\n'
                          f'Seu Saldo Atual é de: {saldo_atual}')

                else:

                    saldo_atual = saldo_atual - saque

                    print(f'Você Depositou: R${saque:.2f}\n'
                          f'Seu Saldo Atual é de: R${saldo_atual:.2f}')

            elif opcao == 3:
                print(f'Seu Saldo Atual é de: {saldo_atual}')

        else:
            print(f'Você Digitou {opcao}. Que não está 0 e 3.')

    except ValueError:
        print('Digite uma Entrada Válida!')
