import sqlite3

def criar_tabela():
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        codigo TEXT NOT NULL UNIQUE,
        descricao TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        preco REAL NOT NULL
    );
    """)

    conexao.commit()
    conexao.close()

# CREATE
def inserir_usuario(codigo, descricao, quantidade, preco):
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()

    cursor.execute(""" INSERT INTO usuarios (codigo, descricao, quantidade, preco) VALUES (?, ?, ?, ?); """,
                   (codigo, descricao, quantidade, preco))

    print('Produto Cadastrado Com Sucesso!!!')

    conexao.commit()
    conexao.close()

# READ
def listar_usuarios():
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM usuarios;")

    usuarios = cursor.fetchall()

    for i in usuarios:
        print(f'ID: {i[0]} || Código: {i[1]} || Produto: {i[2]} || Quantidade: {i[3]} || Preço: {i[4]}')

    conexao.close()

    return usuarios

# UPDATE
def atualizar_usuario(codigo):
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()

    while True:
        try:
            print('1 - Pela Descrição || 2 - Pela Quantidade || 3 - Pelo Preço')
            opcao = int(input('Digite Uma das Opções: '))

            if opcao == 1:

                nova_descricao = input('Digite Uma nova Descrição: ')

                cursor.execute(""" UPDATE usuarios SET descricao = ? WHERE codigo = ?; """,
                               (nova_descricao, codigo))

                print('Atualizado Com Sucesso!!!')

            if opcao == 2:

                nova_quantidade = int(input('Digite a Nova Quantidade: '))

                cursor.execute(""" UPDATE usuarios SET quantidade = ? WHERE codigo = ?; """,
                               (nova_quantidade, codigo))

                print('Atualizado Com Sucesso!!!')

            if opcao == 3:

                novo_preco = float(input('Digite o Preço o Novo: '))

                cursor.execute(""" UPDATE usuarios SET preco = ? WHERE codigo = ?; """,
                               (novo_preco, codigo))

                print('Atualizado Com Sucesso!!!')

        except ValueError:
            print('Digite uma Opção Válida!!!')

        conexao.commit()
        conexao.close()

# DELETE
def deletar_usuario(codigo):
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM usuarios WHERE codigo = ?;", (codigo,))

    print('Deletado com Sucesso!!!')

    conexao.commit()
    conexao.close()


criar_tabela()


while True:
    try:
        print('==== X Menu X ====\n'
              '1 - Inserir Usuários\n'
              '2 - Listar Usuários\n'
              '3 - Atualizar\n'
              '4 - Deletar\n'
              '0 - Fim do Programa\n')

        opcao = int(input('Digite Uma das Opções: '))
        if opcao > 4:
            print(f'Você Digitou {opcao}. Que não está entre 0 e 4.')

        if opcao < 0:
            print(f'Você Digitou um Número Negativo. Que não está entre 0 e 4.')

        if opcao == 1:

            codigo = input('Digite o Código: ')
            descricao = input('Digite a Descrição: ')
            quantidade = int(input('Digite a Quantidade: '))
            preco = float(input('Digite o Preço: '))

            inserir_usuario(codigo, descricao, quantidade, preco)

        if opcao == 2:
            listar_usuarios()

        if opcao == 3:
            codigo = input('Digite o Código do Produto: ')

            atualizar_usuario(codigo)

        if opcao == 4:

            codigo = input('Digite o Código do Produto: ')

            deletar_usuario(codigo)

        if opcao == 0:
            print('Fim do Programa!!!')
            break

    except ValueError:
        print('Digite uma Opção Válida!!!')
