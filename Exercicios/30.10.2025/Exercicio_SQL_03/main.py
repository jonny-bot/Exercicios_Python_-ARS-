import sqlite3


def criar_tabela():
    conn = sqlite3.connect('meu_banco.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        codigo TEXT NOT NULL UNIQUE,
        descricao TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        preco REAL NOT NULL
    )
    ''')
    conn.commit()
    conn.close()


def inserir_dados(codigo, descricao, quantidade, preco):
    conn = sqlite3.connect('meu_banco.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO produtos (codigo, descricao, quantidade, preco)
        VALUES (?, ?, ?, ?)
    ''', (codigo, descricao, quantidade, preco))
    conn.commit()
    conn.close()


criar_tabela()


while True:
    print('Selecione... 1 - Colocar Dados na Tabela: ')

    opcao = int(input('Digite um Número: '))

    if opcao == 1:

        codigo = input('Digite um Código: ')
        descricao = input('Digite o Nome do Produto: ')
        quantidade = int(input('Digite a Quantidade do Produto: '))
        preco = float(input('Digite o Preço do Produto: '))

        inserir_dados(codigo, descricao, quantidade, preco)
        print("Produto inserido com sucesso!")
