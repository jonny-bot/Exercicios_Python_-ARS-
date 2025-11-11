saldo_inicial = float(input('Digite o Saldo Inicial: '))

saldo_atual = saldo_inicial

extrato = []

while True:
    try:
        opcao = int(input('1 - Fazer Saque || 2 - Fazer Depósitos || 3 - Tirar Extrato || 0 - Sair do Programa\n'
                          'Digite uma das Opções: '))

        if opcao not in (0, 1, 2, 3):
            print(f'Você digitou {opcao}. Que não está entre 0 e 3')

        if opcao == 0:
            print('Fim do Programa!!!')
            break

        if opcao == 1:

            print(f'Seu Saldo Atual é de: {saldo_atual}')

            saque = float(input('Digite o Total a Ser Sacado: '))

            saldo_atual = saldo_atual - saque

            temp = 'Saque: ' + str(saque)
            extrato.append(temp)

            print(f'Saque Realizado com sucesso. Seu saldo atual é de: {saldo_atual}')

        if opcao == 2:

            print(f'Seu Saldo Atual é de: {saldo_atual}')

            deposito = float(input('Digite o Total a Ser Depositado: '))

            saldo_atual = saldo_atual + deposito

            temp = 'Deposito: ' + str(deposito)
            extrato.append(temp)

            print(f'Deposito Realizado com sucesso. Seu saldo atual é de: {saldo_atual}')

        if opcao == 3:

            for i in extrato:
                print(i)

            print(f'Saldo Atual: {saldo_atual}')

    except ValueError:
        print('Digite uma Entrada Valida!!!')
