import sqlite3


def criar_banco():
    conexao = sqlite3.connect('meu_banco.db')
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS conta_bancaria (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_conta TEXT NOT NULL UNIQUE,
            senha_conta TEXT NOT NULL,
            saldo_conta REAL NOT NULL
        )''')

    conexao.commit()
    conexao.close()


def criar_conta(nome_conta, senha_conta, saldo_inicial):
    conexao = sqlite3.connect('meu_banco.db')
    cursor = conexao.cursor()

    cursor.execute(''' INSERT INTO conta_bancaria (nome_conta, senha_conta, saldo_conta) VALUES (?, ?, ?)''',
                   (nome_conta, senha_conta, saldo_inicial))

    conexao.commit()
    conexao.close()

    print('Conta Cadastrada com Sucesso!!!')


def visualizar_dados(nome_conta, senha_conta):
    conexao = sqlite3.connect('meu_banco.db')
    cursor = conexao.cursor()

    cursor.execute('''
        SELECT id, nome_conta, senha_conta, saldo_conta FROM conta_bancaria WHERE nome_conta = ? AND senha_conta = ?''',
                   (nome_conta, senha_conta))

    resultado = cursor.fetchall()

    for i in resultado:
        print(f"ID: {i[0]} || NOME CONTA: {i[1]} || SENHA: {i[2]} || SALDO: {i[3]}")

    conexao.close()


def fazer_deposito(nome_conta, senha_conta):
    conexao = sqlite3.connect('meu_banco.db')
    cursor = conexao.cursor()

    cursor.execute(''' SELECT saldo_conta FROM conta_bancaria WHERE nome_conta = ? AND senha_conta = ?''',
                   (nome_conta, senha_conta))

    resultado = cursor.fetchone()

    if resultado:

        saldo_atual = resultado[0]

        try:
            valor_deposito = float(input('Digite o valor a ser depositado: '))

            if valor_deposito <= 0:
                print('O valor do depósito deve ser positivo.')

            else:

                novo_saldo = saldo_atual + valor_deposito

                cursor.execute(''' UPDATE conta_bancaria SET saldo_conta = ? WHERE nome_conta = ? AND senha_conta = ?''',
                               (novo_saldo, nome_conta, senha_conta))

                conexao.commit()

                print(f'Depósito realizado com sucesso! Novo saldo: R$ {novo_saldo:.2f}')

        except ValueError:
            print('Valor inválido. Digite um número válido.')
    else:

        print('Conta não encontrada ou senha incorreta.')

    conexao.close()


def fazer_saque(nome_conta, senha_conta):
    conexao = sqlite3.connect('meu_banco.db')
    cursor = conexao.cursor()

    cursor.execute(''' SELECT saldo_conta FROM conta_bancaria WHERE nome_conta = ? AND senha_conta = ?''',
                   (nome_conta, senha_conta))

    resultado = cursor.fetchone()

    if resultado:

        saldo_atual = resultado[0]

        try:

            valor_saque = float(input('Digite o valor a ser sacado: '))

            if valor_saque <= 0:

                print('O valor do saque deve ser positivo.')

            elif valor_saque > saldo_atual:

                print('Saldo insuficiente para realizar o saque.')

            else:
                novo_saldo = saldo_atual - valor_saque

                cursor.execute(''' UPDATE conta_bancaria SET saldo_conta = ? WHERE nome_conta = ? AND senha_conta = ?''',
                               (novo_saldo, nome_conta, senha_conta))

                conexao.commit()
                print(f'Saque realizado com sucesso! Novo saldo: R$ {novo_saldo:.2f}')

        except ValueError:
            print('Valor inválido. Digite um número válido.')

    else:
        print('Conta não encontrada ou senha incorreta.')

    conexao.close()


criar_banco()


while True:
    try:
        opcao = int(input('0 - Sair do Programa\n'
                          '1 - Criar Uma Conta\n'
                          '2 - Visualizar Dados da Conta\n'
                          '3 - Fazer Depósito\n'
                          '4 - Fazer Saque\n'
                          'Digite uma das opções: '))

        if opcao == 0:

            print('Fim do Programa!!!')
            break

        elif opcao == 1:

            nome_conta = input('Digite o Nome da Conta: ')
            senha_conta = input('Digite a sua Senha: ')
            saldo_inicial = float(input('Digite o Saldo Inicial: '))
            criar_conta(nome_conta, senha_conta, saldo_inicial)

        elif opcao == 2:

            nome_conta = input('Digite o Nome da Conta: ')
            senha_conta = input('Digite a sua Senha: ')
            visualizar_dados(nome_conta, senha_conta)

        elif opcao == 3:

            nome_conta = input('Digite o Nome da Conta: ')
            senha_conta = input('Digite a sua Senha: ')
            fazer_deposito(nome_conta, senha_conta)

        elif opcao == 4:

            nome_conta = input('Digite o Nome da Conta: ')
            senha_conta = input('Digite a sua Senha: ')
            fazer_saque(nome_conta, senha_conta)

        else:
            print('Opção inválida. Tente novamente.')

    except ValueError:
        print('Digite uma Entrada Válida!!!')
