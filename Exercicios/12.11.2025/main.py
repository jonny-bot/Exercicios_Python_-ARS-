from datetime import datetime

valor_inicial = float(input('Digite o Valor inicial: '))

agora = datetime.now()

extrato = []

saldo_atual = valor_inicial

while True:
    try:
        opcao = int(input('0 - Sair do Programa || 1 - Tirar Dinheiro || 2 - Depositar || 3 - Tirar Extrato\n'
                          'Digite umas das Opções: '))

        if opcao > 2:
            print(f'Você digitou {opcao}. Que não está entre 0 e 2.')

        if opcao == 0:
            print('Fim do Programa!!!')
            break

        if opcao == 1:

            print(f'Seu Saldo Atual é de: {saldo_atual}')

            saque = float(input('Digite quanto você vai tirar: '))

            if saque > saldo_atual:
                print('Você não tem Saldo Suficiente.')

            else:

                saldo_atual = saldo_atual - saque

                temp = 'Saque: ' + str(saque) + ' Data/Hora: ' + agora.strftime("%d/%m/%Y, %H:%M:%S")
                extrato.append(temp)

                print('Saque Realizado com Sucesso!!!')

        if opcao == 2:

            print(f'Seu Saldo Atual é de: {saldo_atual}')

            deposito = float(input('Digite quanto você vai tirar: '))

            saldo_atual = saldo_atual - deposito

            temp = 'Deposito: ' + str(deposito) + ' Data/Hora: ' + agora.strftime("%d/%m/%Y, %H:%M:%S")
            extrato.append(temp)

            print('Deposito Realizado com Sucesso!!!')

        if opcao == 3:

            for i in extrato:
                print(f'{i}')

            print(f'Seu Saldo Atual eh: {saldo_atual}')

    except ValueError:
        print('Digite uma Entrada Válida!!!')
