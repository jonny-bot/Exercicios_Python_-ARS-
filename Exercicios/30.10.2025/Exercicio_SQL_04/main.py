import sqlite3


def criar_banco():
    conexao = sqlite3.connect('meu_banco.db')
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo TEXT NOT NULL UNIQUE,
            descricao TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            preco REAL NOT NULL
        )''')

    conexao.commit()
    conexao.close()
    print('Banco Criado!!!')


def inserir_dados(codigo, descricao, quantidade, preco):
    conexao = sqlite3.connect('meu_banco.db')
    cursor = conexao.cursor()
    cursor.execute(''' INSERT INTO produtos (codigo, descricao, quantidade, preco) 
    VALUES (?, ?, ?, ?) ''', (codigo, descricao, quantidade, preco))

    conexao.commit()
    conexao.close()

criar_banco()

while True:
    print('Selecione... 1 - Inserir Dados || 2 - Sair')

    opcao = int(input('Digite a Opção: '))

    if opcao == 1:

        codigo = input('Digite um Código: ')
        descricao = input('Digite o Nome do Produto: ')
        quantidade = int(input('Digite a Quantidade de Produto: '))
        preco = float(input('Digite o Preço do Produto: '))

        inserir_dados(codigo, descricao, quantidade, preco)
        print('Dados Adicionados com Sucesso!!!')

    elif opcao == 2:
        print('Fim do Programa!!!')
        break