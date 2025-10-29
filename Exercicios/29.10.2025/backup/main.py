import sqlite3


def criar_tabela():
    conn = sqlite3.connect('conta_bancaria.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        senha TEXT NOT NULL,
        saldo INTEGER NOT NULL
    )
    ''')
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
        print("Conta cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        print("Conta já cadastrado.")
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


def sacar_depositar():
    conn = sqlite3.connect('conta_bancaria.db')
    cursor = conn.cursor()

    nome_input = input("Digite seu nome: ")
    senha_input = input("Digite sua senha: ")

    consulta = "SELECT * FROM usuarios WHERE nome = ? AND senha = ?"
    cursor.execute(consulta, (nome_input, senha_input))
    resultado = cursor.fetchone()

    saldo_atual = resultado[3]
    print(f"Seu saldo atual é: R$ {saldo_atual:.2f}")

    print('Digite: 1 - Saque || 2 - Depositar')

    opcao = int(input('Digite a Opção: '))

    if opcao == 1:
        saque = float(input("Quanto você quer sacar: "))
        if saque <= saldo_atual:
            novo_saldo = saldo_atual - saque
            cursor.execute("UPDATE usuarios SET saldo = ? WHERE nome = ?", (novo_saldo, nome_input))
            conn.commit()
            print(f"Saque de R$ {saque:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente para o saque.")

    if opcao == 2:
        deposito = float(input("Quanto você quer depositar: "))
        novo_saldo = saldo_atual + deposito
        cursor.execute("UPDATE usuarios SET saldo = ? WHERE nome = ?", (novo_saldo, nome_input))
        conn.commit()
        print(f"Saque de R$ {deposito:.2f} realizado com sucesso.")


criar_tabela()


while True:
    print('1 - Criar Conta || 2 - Listar Dados || 3 - Autenticar || 4 - Sacar/Depositar || 5 - Sair')
    try:
        opcoes = int(input('Digite uma opção: '))
        if opcoes == 1:
            criar_conta()
        elif opcoes == 2:
            listar_usuarios()
        elif opcoes == 3:
            autenticas_usuario()
        elif opcoes == 4:
            sacar_depositar()
        elif opcoes == 5:
            print("Encerrando o programa.")
            break
        else:
            print('Opção Inválida')
    except ValueError:
        print('Digite um número válido.')
