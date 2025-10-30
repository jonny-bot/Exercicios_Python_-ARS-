import sqlite3
from datetime import datetime


def criar_tabela():
    conn = sqlite3.connect('conta_bancaria.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        senha TEXT NOT NULL,
        saldo REAL NOT NULL
    )
    ''')
    conn.commit()
    conn.close()


def criar_tabela_historico():
    conn = sqlite3.connect('conta_bancaria.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS historico_transacoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        tipo TEXT NOT NULL,
        valor REAL NOT NULL,
        data TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()


def registrar_transacao(nome, tipo, valor):
    conn = sqlite3.connect('conta_bancaria.db')
    cursor = conn.cursor()

    data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('''
        INSERT INTO historico_transacoes (nome, tipo, valor, data)
        VALUES (?, ?, ?, ?)
    ''', (nome, tipo, valor, data))
    conn.commit()
    conn.close()


def criar_conta():
    conn = sqlite3.connect('conta_bancaria.db')
    cursor = conn.cursor()

    nome = input('Digite o seu Nome: ')
    senha = input('Digite a sua Senha: ')
    saldo = float(input('Digite o seu Saldo: '))

    try:
        cursor.execute("INSERT INTO usuarios (nome, senha, saldo) VALUES (?, ?, ?)",
                       (nome, senha, saldo))
        conn.commit()
        print("Conta cadastrada com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro ao cadastrar conta.")
    conn.close()


def listar_usuarios():
    conn = sqlite3.connect('conta_bancaria.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()

    for usuario in usuarios:
        print(f"ID: {usuario[0]} | Nome: {usuario[1]} | Saldo: R${usuario[3]:.2f}")

    conn.close()


def autenticas_usuario():
    conn = sqlite3.connect('conta_bancaria.db')
    cursor = conn.cursor()

    nome_input = input("Digite seu nome: ")
    senha_input = input("Digite sua senha: ")

    consulta = "SELECT * FROM usuarios WHERE nome = ? AND senha = ?"
    cursor.execute(consulta, (nome_input, senha_input))
    resultado = cursor.fetchone()

    if resultado:
        print("Usuário autenticado com sucesso!")
    else:
        print("Nome ou senha incorretos.")

    conn.close()


def sacar():
    conn = sqlite3.connect('conta_bancaria.db')
    cursor = conn.cursor()

    nome_input = input("Digite seu nome: ")
    senha_input = input("Digite sua senha: ")

    cursor.execute("SELECT * FROM usuarios WHERE nome = ? AND senha = ?", (nome_input, senha_input))
    resultado = cursor.fetchone()

    if resultado:
        saldo_atual = resultado[3]
        print(f"Seu saldo atual é: R$ {saldo_atual:.2f}")

        saque = float(input("Quanto você quer sacar: "))
        if saque <= saldo_atual:
            novo_saldo = saldo_atual - saque
            cursor.execute("UPDATE usuarios SET saldo = ? WHERE nome = ?", (novo_saldo, nome_input))
            conn.commit()
            print(f"Saque de R$ {saque:.2f} realizado com sucesso.")
            registrar_transacao(nome_input, 'saque', saque)
        else:
            print("Saldo insuficiente para o saque.")
    else:
        print("Usuário não encontrado ou senha incorreta.")

    conn.close()


def depositar():
    conn = sqlite3.connect('conta_bancaria.db')
    cursor = conn.cursor()

    nome_input = input("Digite seu nome: ")
    senha_input = input("Digite sua senha: ")

    cursor.execute("SELECT * FROM usuarios WHERE nome = ? AND senha = ?", (nome_input, senha_input))
    resultado = cursor.fetchone()

    if resultado:
        saldo_atual = resultado[3]
        print(f"Seu saldo atual é: R$ {saldo_atual:.2f}")

        deposito = float(input("Quanto você quer depositar: "))
        novo_saldo = saldo_atual + deposito
        cursor.execute("UPDATE usuarios SET saldo = ? WHERE nome = ?", (novo_saldo, nome_input))
        conn.commit()
        print(f"Depósito de R$ {deposito:.2f} realizado com sucesso.")
        registrar_transacao(nome_input, 'deposito', deposito)
    else:
        print("Usuário não encontrado ou senha incorreta.")

    conn.close()


def extrato():
    conn = sqlite3.connect('conta_bancaria.db')
    cursor = conn.cursor()

    nome_input = input("Digite seu nome para ver o extrato: ")

    cursor.execute('''
        SELECT tipo, valor, data FROM historico_transacoes WHERE nome = ? ORDER BY data DESC ''', (nome_input,))
    transacoes = cursor.fetchall()

    if transacoes:
        print(f"\nExtrato de {nome_input}:")
        for tipo, valor, data in transacoes:
            print(f"{data} | {tipo.capitalize():<10} | R$ {valor:.2f}")
    else:
        print("Nenhuma transação encontrada.")

    conn.close()


criar_tabela()
criar_tabela_historico()

while True:
    print('1 - Criar Conta || 2 - Listar Dados || 3 - Autenticar || 4 - Sacar || 5 - Depositar || 6 - Extrato || 7 - Sair')
    try:
        opcoes = int(input('Digite uma opção: '))
        if opcoes == 1:
            criar_conta()
        elif opcoes == 2:
            listar_usuarios()
        elif opcoes == 3:
            autenticas_usuario()
        elif opcoes == 4:
            sacar()
        elif opcoes == 5:
            depositar()
        elif opcoes == 6:
            extrato()
        elif opcoes == 7:
            print("Encerrando o programa.")
            break
        else:
            print('Opção Inválida')
    except ValueError:
        print('Digite um número válido.')
