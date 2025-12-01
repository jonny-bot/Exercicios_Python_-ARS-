valor_inicial = int(input('Digite o Valor Inicial: '))

valor_carteira = valor_inicial

valor_banco = 0

print(f'Você tem R${valor_carteira:.2f} na sua Carteira.\n'
      f'Você tem R${valor_banco:.2f} no Banco.')

while True:
    try:
        opcao = int(input('0 - Sair do Programa\n'
                          '1 - Realizar Depósito\n'
                          '2 - Realizar Saque\n'
                          'Digite uma das Opções: '))

        if 0 <= opcao <= 2:

            if opcao == 0:
                print('Saindo do Programa...')
                break

            elif opcao == 1:

                print('====x SALDO x====\n'
                      
                      f'Carteira: R${valor_carteira:.2f}\n'
                      f'Banco: R${valor_banco:.2f}')

                deposito = float(input('Digite o Valor a Ser Depositado: '))

                if deposito <= valor_carteira:

                    valor_carteira -= deposito
                    valor_banco += deposito

                    print(f'Depósito de R${deposito:.2f} realizado com sucesso!')

                else:
                    print('Saldo insuficiente na Carteira!')

            elif opcao == 2:

                print('====x SALDO x====\n'
                      
                      f'Carteira: R${valor_carteira:.2f}\n'
                      f'Banco: R${valor_banco:.2f}')

                saque = float(input('Digite o Valor a Ser Sacado: '))

                if saque <= valor_banco:

                    valor_banco -= saque
                    valor_carteira += saque

                    print(f'Saque de R${saque:.2f} realizado com sucesso!')

                else:
                    print('Saldo insuficiente no Banco!')

        else:
            print(f'Você Digitou: {opcao}. Que não está Entre 0 e 2.')

    except ValueError:
        print('Digite uma Entrada Válida!')
