import sqlite3

def criar_banco_usuarios():
    conexao = sqlite3.connect('conta_bancaria.db')
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS conta_bancaria(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL,
            saldo REAL NOT NULL,
            contador INTEGER NOT NULL,
            bloqueado TEXT NOT NULL DEFAULT 'N'
        )
    ''')

    conexao.commit()
    conexao.close()


def criar_conta(criar_nome, criar_senha, criar_saldo):
    conexao = sqlite3.connect('conta_bancaria.db')
    cursor = conexao.cursor()

    cursor.execute('''
        INSERT INTO conta_bancaria (nome, senha, saldo, contador, bloqueado)
        VALUES (?, ?, ?, ?, ?)''', (criar_nome, criar_senha, criar_saldo, 0, 'N'))

    conexao.commit()
    conexao.close()

    print('Conta criada com sucesso!')


def liberar_acesso():
    conexao = sqlite3.connect('conta_bancaria.db')
    cursor = conexao.cursor()

    conta_desbloqueado = input('Digite o Nome da Conta a Ser Desbloqueada: ')

    cursor.execute('UPDATE conta_bancaria SET contador = 0, bloqueado = ? WHERE nome = ?', ('N', conta_desbloqueado))

    conexao.commit()
    conexao.close()


def emitir_extrato(nome_conta):
    conexao = sqlite3.connect('conta_bancaria.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM conta_bancaria WHERE nome = ?", (nome_conta,))
    resultado = cursor.fetchone()

    if resultado:
        print(f"Extrato da Conta:\n"
              f"Nome da Conta: {resultado[1]} \nSaldo Atual: R$ {resultado[3]:.2f}")

    conexao.commit()
    conexao.close()


def fazer_login(login_nome, login_senha):
    conexao = sqlite3.connect('conta_bancaria.db')
    cursor = conexao.cursor()

    cursor.execute('SELECT nome, senha, contador, bloqueado FROM conta_bancaria WHERE nome = ?', (login_nome,))
    resultado = cursor.fetchone()

    if not resultado:
        print('Usuário não encontrado!')
        conexao.close()
        return False

    nome, senha_correta, contador, bloqueado = resultado

    if bloqueado == 'S':
        print('Usuário bloqueado!')
        conexao.close()
        return False

    if login_senha == senha_correta:
        print('Login realizado com sucesso!')
        cursor.execute("UPDATE conta_bancaria SET contador = 0 WHERE nome = ?", (login_nome,))

        conexao.commit()
        conexao.close()

        return True

    else:
        contador += 1
        print(f"Senha incorreta. Tentativas: {contador}/3")

        if contador >= 3:
            cursor.execute("UPDATE conta_bancaria SET contador = ?, bloqueado = ? WHERE nome = ?", (contador, 'S', login_nome))
            print("Usuário bloqueado por excesso de tentativas.")
        else:
            cursor.execute("UPDATE conta_bancaria SET contador = ? WHERE nome = ?", (contador, login_nome))

        conexao.commit()
        conexao.close()

        return False


def realizar_saque(nome_saque):
    conexao = sqlite3.connect('conta_bancaria.db')
    cursor = conexao.cursor()

    cursor.execute('SELECT saldo FROM conta_bancaria WHERE nome = ?', (nome_saque,))
    resultado = cursor.fetchone()

    if resultado:

        saldo_atual = resultado[0]

        print(f"Saldo atual: R$ {saldo_atual:.2f}")

        valor_sacado = float(input("Valor do saque: "))

        if valor_sacado <= saldo_atual:

            novo_saldo = saldo_atual - valor_sacado

            cursor.execute('UPDATE conta_bancaria SET saldo = ? WHERE nome = ?', (novo_saldo, nome_saque))

            print("Saque realizado com sucesso!")

        else:
            print("Saldo insuficiente.")

    else:
        print("Usuário não encontrado.")

    conexao.commit()
    conexao.close()


def realizar_deposito(nome_deposito):
    conexao = sqlite3.connect('conta_bancaria.db')
    cursor = conexao.cursor()

    valor_depositado = float(input("Valor do depósito: "))

    cursor.execute('UPDATE conta_bancaria SET saldo = saldo + ? WHERE nome = ?', (valor_depositado, nome_deposito))

    conexao.commit()
    conexao.close()

    print("Depósito realizado com sucesso!")


def realizar_transferencia(nome_transferencia):
    conexao = sqlite3.connect('conta_bancaria.db')
    cursor = conexao.cursor()

    cursor.execute('SELECT saldo FROM conta_bancaria WHERE nome = ?', (nome_transferencia,))

    resultado = cursor.fetchone()

    valor_transferido = 0.0
    limite_por_dia = 2000.00

    if resultado:

        saldo_atual = resultado[0]

        print(f"Saldo atual: R$ {saldo_atual:.2f}")

        valor_transferido = float(input("Qual o valor a ser transferido: "))

        if valor_transferido <= saldo_atual and valor_transferido <= limite_por_dia:

            novo_saldo = saldo_atual - valor_transferido

            cursor.execute('UPDATE conta_bancaria SET saldo = ? WHERE nome = ?', (novo_saldo, nome_transferencia))

        else:
            print("Saldo insuficiente ou limite diário excedido.")

            conexao.close()

            return

    else:
        print("Usuário não encontrado.")

        conexao.close()

        return

    para_transferir = input("Transferir para qual conta: ")

    cursor.execute('SELECT saldo FROM conta_bancaria WHERE nome = ?', (para_transferir,))

    resultado_2 = cursor.fetchone()

    if resultado_2:

        saldo_atual_2 = resultado_2[0]

        novo_saldo_2 = saldo_atual_2 + valor_transferido

        cursor.execute('UPDATE conta_bancaria SET saldo = ? WHERE nome = ?', (novo_saldo_2, para_transferir))

        print("Transferência realizada com sucesso!")
    else:

        print('Usuário de destino não encontrado.')

        cursor.execute('UPDATE conta_bancaria SET saldo = saldo + ? WHERE nome = ?', (valor_transferido, nome_transferencia))

    conexao.commit()
    conexao.close()


def conta_logada(nome_conta):
    while True:
        try:
            print('1 - Realizar Saque\n'
                  '2 - Realizar Depósito\n'
                  '3 - Realizar Transferências\n'
                  '4 - Tirar Extrato\n'
                  '0 - Sair')

            opcao = int(input('Escolha uma das opções: '))

            if opcao not in (0, 1, 2, 3, 4):
                print('Digite uma opção válida!')
                continue

            if opcao == 1:
                realizar_saque(nome_conta)

            elif opcao == 2:
                realizar_deposito(nome_conta)

            elif opcao == 3:
                realizar_transferencia(nome_conta)

            elif opcao == 4:
                emitir_extrato(nome_conta)

            elif opcao == 0:
                print("Saindo da conta!")
                break

        except ValueError:
            print("Digite um número válido.")


def inicio_programa():
    criar_banco_usuarios()

    while True:
        try:
            print('1 - Criar Conta || 2 - Fazer Login || 3 - Liberar Acesso || 0 - Sair')
            opcao = int(input('Escolha uma opção: '))

            if opcao not in (0, 1, 2, 3):
                print('Digite uma opção válida!')
                continue

            if opcao == 1:
                criar_nome = input('Digite o nome da conta: ')
                criar_senha = input('Digite a senha da conta: ')
                criar_saldo = float(input('Qual o saldo inicial: '))
                criar_conta(criar_nome, criar_senha, criar_saldo)

            elif opcao == 2:
                login_nome = input('Digite o nome da conta: ')
                login_senha = input('Digite a senha da conta: ')
                if fazer_login(login_nome, login_senha):
                    conta_logada(login_nome)

            elif opcao == 3:
                liberar_acesso()

            elif opcao == 0:
                print("Fim do programa!")
                break

        except ValueError:
            print("Digite um número válido.")


inicio_programa()
