import sqlite3

def criar_banco():
    conexao = sqlite3.connect('conta_bancaria.db')
    cursor = conexao.cursor()


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS conta_bancaria(
            id INTEGER PRIMARY KEY AUTOINCREMENT,  
            nome TEXT NOT NULL UNIQUE,           
            senha TEXT NOT NULL,         
            saldo_inicial REAL NOT NULL                    
        )''')

    conexao.commit()
    conexao.close()


def criar_contas(nome, senha, saldo_inicial):
    conexao = sqlite3.connect('conta_bancaria.db')
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO conta_bancaria (nome, senha, saldo_inicial) "
                   "VALUES (?, ?, ?)",(nome, senha, saldo_inicial))

    print('Conta Criado com Sucesso!!!')

    conexao.commit()
    conexao.close()


def autenticar_usuario(nome_autenticado, senha_autenticado):
    conexao = sqlite3.connect('conta_bancaria.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM conta_bancaria WHERE nome = ? AND senha = ?", (nome_autenticado, senha_autenticado))
    resultado = cursor.fetchone()

    conexao.close()

    if resultado:
        print('Usuário autenticado com sucesso!')
        return True
    else:
        print('Usuário ou senha incorretos!')
        return False


def sacar(nome_saque):
    conn = sqlite3.connect('conta_bancaria.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM conta_bancaria WHERE nome = ?", (nome_saque, ))
    resultado = cursor.fetchone()

    if resultado:
        saldo_atual = resultado[3]
        print(f"Seu saldo atual é: R$ {saldo_atual:.2f}")

        saque = float(input("Quanto você quer sacar: "))
        if saque <= saldo_atual:
            novo_saldo = saldo_atual - saque
            cursor.execute("UPDATE conta_bancaria SET saldo_inicial = ? WHERE nome = ?", (novo_saldo, nome_saque))
            conn.commit()
            print(f"Saque de R$ {saque:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente para o saque.")
    else:
        print("Usuário não encontrado.")

    conn.close()


def depositar(nome_depositar):
    conn = sqlite3.connect('conta_bancaria.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM conta_bancaria WHERE nome = ?", (nome_depositar, ))
    resultado = cursor.fetchone()

    saldo_atual = resultado[3]
    print(f"Seu saldo atual é: R$ {saldo_atual:.2f}")

    depitar = float(input("Quanto você quer depositar: "))
    novo_saldo = saldo_atual + depitar
    cursor.execute("UPDATE conta_bancaria SET saldo_inicial = ? WHERE nome = ?", (novo_saldo, nome_depositar))
    conn.commit()
    print(f"Saque de R$ {depitar:.2f} realizado com sucesso.")

    conn.close()


def transferir_dinheiro(origem,destino):
    conn = sqlite3.connect('conta_bancaria.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM conta_bancaria WHERE nome = ?", (origem,))
    resultado = cursor.fetchone()

    saldo_atual = resultado[3]
    print(f"Seu saldo atual é: R$ {saldo_atual:.2f}")

    # Continuar amanhã

    conn.commit()
    conn.close()


criar_banco()


while True:
    try:
        print('1 - Criar Uma Conta\n'
              '2 - Autenticar Usuário\n'
              '3 - Realizar Saques\n'
              '4 - Realizar Depósitos\n'
              '5 - Realizar Transferência\n'
              '6 - Fim do Programa\n')

        opcoes = int(input('Digite uma das Opções: '))

        if opcoes == 1:
            nome = input('Digite um Nome: ')
            senha = input('Digite uma Senha: ')
            saldo_inicial = float(input('Digite um Valor Inicial: '))

            criar_contas(nome, senha, saldo_inicial)

        if opcoes == 2:
            nome_autenticado = input('Digite um Nome: ')
            senha_autenticado = input('Digite uma Senha: ')

            autenticar_usuario(nome_autenticado, senha_autenticado)

        if opcoes == 3:
            nome_saque = input("Digite Seu Nome: ")
            sacar(nome_saque)

        if opcoes == 4:
            nome_depositar = input("Digite seu nome: ")
            depositar(nome_depositar)

        if opcoes == 5:
            origem = input('Digite um Nome: ')
            transferir_dinheiro(origem)

        if opcoes == 6:
            print('Fim do Programa!!!')
            break

    except ValueError:
        print('Digite uma Entrada Valida!!!')