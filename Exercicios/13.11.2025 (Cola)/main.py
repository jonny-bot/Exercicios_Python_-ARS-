saldo_inicial = float(input('Digite o Saldo Inicial: '))

saldo_atual = saldo_inicial

extrato = []

while True:
    try:
        opcao = int(input('0 - Sair do Programa\n'
                          '1 - Sacar Dinheiro\n'
                          '2 - Depositar Dinheiro\n'
                          '3 - Tirar Extrato\n'
                          'Digite uma das Opções: '))

        if opcao > 3:
            print(f'Você Digitou {opcao}. Que não está entre 0 e 3.')

        if opcao == 0:
            print('Fim do Programa!!!')
            break

        if opcao == 1:

            print(f'O seu Saldo Atual eh de: {saldo_atual:.2f}')

            saque = float(input('Digite o Total a Ser Sacado: '))

            if saque > saldo_atual:

                print('Saldo Insuficiente!!!')

            else:

                saldo_atual = saldo_atual - saque

                temp = 'Saque: R$' + str(saque)
                extrato.append(temp)

                print('Saque Realizado com Sucesso!!!')

                print(f'O seu Saldo Atual eh de: {saldo_atual:.2f}')

        if opcao == 2:

            print(f'O seu Saldo Atual eh de: {saldo_atual:.2f}')

            deposito = float(input('Digite o Total a Ser Depositado: '))

            saldo_atual = saldo_atual + deposito

            temp = 'Deposito: R$' + str(deposito)
            extrato.append(temp)

            print('Deposito Realizado com Sucesso!!!')

            print(f'O seu Saldo Atual eh de: {saldo_atual:.2f}')

        if opcao == 3:

            for i in extrato:
                print(f'{i}')

            print(f'Saldo Atual: {saldo_atual:.2f}')

    except ValueError:
        print('Digite Uma Entrada Válida!!!')

print(f'Saldo Atual: {saldo_atual:.2f}')
