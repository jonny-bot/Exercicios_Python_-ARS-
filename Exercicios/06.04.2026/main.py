import sqlite3


# Cria e Conecta ao banco
def conexao_cursor():
    conexao = sqlite3.connect('meu_banco.db')
    cursor = conexao.cursor()
    return conexao, cursor


# Criar Tabela
def criar_tabela():
    conexao, cursor = conexao_cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo TEXT NOT NULL UNIQUE,
            descricao TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            preco REAL NOT NULL
        )
    ''')

    conexao.commit()
    conexao.close()


# Inserir Dados
def inserir_dados(codigo, descricao, quantidade, preco):
    conexao, cursor = conexao_cursor()

    cursor.execute("INSERT INTO produtos (codigo, descricao, quantidade, preco) "
                   "VALUES (?, ?, ?, ?)", (codigo, descricao, quantidade, preco))

    print('Dados Inseridos Com Sucesso!!!')

    conexao.commit()
    conexao.close()


# Consultar Dados
def consultar_dados():
    conexao, cursor = conexao_cursor()

    try:
        lista_consulta = [
            'Sair do Programa',
            'Selecionar a Tabela Toda',
            'Id do Produto',
            'Código do Produto',
            'Descrição do Produto',
            'Quantidade do Produto',
            'Preço do Produto'
        ]

        for cont, listar in enumerate(lista_consulta):
            print(f'{cont} - {listar}')

        opcao_consulta = int(input('Digite uma das Opções: '))

        match opcao_consulta:

            case 0:
                print('Saindo do Programa...')

            case 1:
                cursor.execute("SELECT * FROM produtos")

            case 2:
                produto_id = int(input('Digite o ID do Produto: '))
                cursor.execute("SELECT * FROM produtos WHERE id = ?", (produto_id,))

            case 3:
                produto_codigo = input('Digite o Código do Produto: ')
                cursor.execute("SELECT * FROM produtos WHERE codigo = ?", (produto_codigo,))

            case 4:
                produto_descricao = input('Digite a Descrição do Produto: ')
                cursor.execute("SELECT * FROM produtos WHERE descricao = ?", (produto_descricao,))

            case 5:
                produto_quantidade = int(input('Digite a Quantidade do Produto: '))
                cursor.execute("SELECT * FROM produtos WHERE quantidade = ?", (produto_quantidade,))

            case 6:
                produto_preco = float(input('Digite o Preço do Produto: '))
                cursor.execute("SELECT * FROM produtos WHERE preco = ?", (produto_preco,))

            case _:
                print(f'Opção inválida!')
                return

        resultado = cursor.fetchall()

        for linha in resultado:
            print(f'ID: {linha[0]} || '
                  f'Código: {linha[1]} || '
                  f'Descrição: {linha[2]} || '
                  f'Quantidade: {linha[3]} || '
                  f'Preço: {linha[4]}')

    except ValueError:
        print('Digite uma Entrada Valida!!!')

    finally:
        conexao.close()


# Atualizar Dados
def atualizar_dados():
    conexao, cursor = conexao_cursor()

    try:

        lista_atualizacao = ['Sair do Programa',
                             'Atualizar Descrição',
                             'Atualizar Quantidade',
                             'Atualizar Preço']

        for cont, listar in enumerate(lista_atualizacao):
            print(f'{cont} - {listar}')

        escolha_atualizacao = int(input('Digite uma das Opções: '))

        id_produto = int(input("Digite o ID do produto: "))

        match escolha_atualizacao:

            case 0:
                print('Fim do Programa...')

            case 1:
                nova_descricao = input("Digite a nova descrição: ")
                cursor.execute("UPDATE produtos SET descricao = ? WHERE id = ?", (nova_descricao, id_produto))

            case 2:
                nova_quantidade = int(input("Digite a nova quantidade: "))
                cursor.execute("UPDATE produtos SET quantidade = ? WHERE id = ?", (nova_quantidade, id_produto))

            case 3:
                novo_preco = float(input("Digite o novo preço: "))
                cursor.execute("UPDATE produtos SET preco = ? WHERE id = ?", (novo_preco, id_produto))

            case _:
                print(f'Opção inválida!')
                return

        print('Dados Atualizados Com Sucesso!!!')

        conexao.commit()
        conexao.close()

    except ValueError:
        print('Digite uma Entrada Valida!!!')

    finally:
        conexao.close()


# Deletar Dados
def deletar_dados():
    conexao, cursor = conexao_cursor()

    id_produto = int(input("Digite o ID do produto a deletar: "))

    cursor.execute("DELETE FROM produtos WHERE id = ?", (id_produto,))

    print('Dados Excluídos com Sucesso!!!!')

    conexao.commit()
    conexao.close()


criar_tabela()

while True:
    try:
        lista_crud = [
            'Sair do Programa',
            'Inserir Dados',
            'Consultar Dados',
            'Atualizar Dados',
            'Deletar Dados'
        ]

        for contador, item in enumerate(lista_crud):
            print(f'{contador} - {item}')

        opcao = int(input('Digite uma das Opções: '))

        match opcao:
            case 0:
                print('Saindo do Programa...')
                break

            case 1:
                codigo = input('Digite um Código do Produto: ')
                descricao = input('Digite a Descrição do Produto: ')
                quantidade = int(input('Digite a Quantidade do Produto: '))
                preco = float(input('Digite o Preço do Produto: '))

                inserir_dados(codigo, descricao, quantidade, preco)

            case 2:
                consultar_dados()

            case 3:
                atualizar_dados()

            case 4:
                deletar_dados()

            case _:
                print(f'Você digitou {opcao}, que não está entre 0 e {len(lista_crud) - 1}')

    except ValueError:
        print('Digite uma entrada válida!!!')