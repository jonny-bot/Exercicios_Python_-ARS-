import random
import sqlite3


conexao = sqlite3.connect('nome_banco.db')
cursor = conexao.cursor()


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


def gerar_dados():
    lista = ["Parafuso", "Martelo", "Chave de fenda", "Alicate", "Serrote", "Furadeira", "Broca", "Trena", "Nível", "Lixa", "Tinta", "Pincel", "Rolo de pintura", "Cimento", "Areia", "Tijolo", "Telha", "Válvula", "Canos", "Torneira"]

    gerar_codigo = str(random.randint(1001, 9999))
    gerar_descricao = random.choice(lista)
    gerar_quantidade = random.randint(25, 900)
    gerar_preco = round(random.uniform(59.00, 900.00), 2)

    return gerar_codigo, gerar_descricao, gerar_quantidade, gerar_preco


def colocar_dados():
    conexao = sqlite3.connect('nome_banco.db')
    cursor = conexao.cursor()

    voltas = 0
    quantidade_dados = int(input('Digite a quantidade de Dados: '))

    while voltas < quantidade_dados:
        codigo, descricao, quantidade, preco = gerar_dados()
        cursor.execute(
            "INSERT INTO produtos (codigo, descricao, quantidade, preco) VALUES (?, ?, ?, ?)",
            (codigo, descricao, quantidade, preco)
        )
        voltas += 1

    print('Dados Adicionados com Sucesso!!!')

    conexao.commit()
    conexao.close()


def exibir_dados():
    conexao = sqlite3.connect('nome_banco.db')
    cursor = conexao.cursor()

    print('1 - Mostrar Dados da Tabela || 2 - Consultar Por ID || 3 - Consultar Por Código')

    opcao = int(input('Digite Umas das Opções: '))

    if opcao == 1:
        cursor.execute('SELECT * FROM produtos')
        for i in cursor.fetchall():
            print(f'ID: {i[0]} || Código: {i[1]} || Descrição: {i[2]} || Quantidade:{i[3]} || Preço:{i[4]}')

    if opcao == 2:

        consultar_id = int(input('Digite o ID que quer Consultar: '))

        cursor.execute("SELECT * FROM produtos WHERE id = ?", (consultar_id,))

        resultados = cursor.fetchall()
        for i in resultados:
            print(f"ID: {i[0]} || CODIGO: {i[1]} || DESCRICAO: {i[2]} || QUANTIDADE: {i[3]} || PRECO: {i[4]}")

    if opcao == 3:

        consultar_codigo = str(input('Digite o Código que quer Consultar: '))

        cursor.execute("SELECT * FROM produtos WHERE codigo = ?", (consultar_codigo,))

        resultados = cursor.fetchall()
        for i in resultados:
            print(f"ID: {i[0]} || CODIGO: {i[1]} || DESCRICAO: {i[2]} || QUANTIDADE: {i[3]} || PRECO: {i[4]}")

    conexao.commit()
    conexao.close()


def excluir_dados():
    conexao = sqlite3.connect('nome_banco.db')
    cursor = conexao.cursor()

    print('Deletar Pelo:\n'
          '1 - Pelo ID\n'
          '2 - Pelo Código\n'
          '3 - Apagar Todos os Registro')

    while True:
        opcao = int(input('Digite Umas das Opções: '))

        if opcao == 1:
            excuir_id = int(input('Digite o ID que queira Excluir: '))

            cursor.execute("DELETE FROM nome_tabela WHERE id = ?", (excuir_id,))
            print('Excluido Com Sucesso!!!')


        if opcao == 2:
            excuir_codigo = int(input('Digite o Código que queira Excluir: '))

            cursor.execute("DELETE FROM nome_tabela WHERE codigo = ?", (excuir_codigo,))
            print('Excluido Com Sucesso!!!')


        if opcoes == 3:
            cursor.execute("DELETE FROM produtos")
            cursor.execute("DELETE FROM sqlite_sequence WHERE name='produtos'")

            print('Excluido Com Sucesso!!!')

        conexao.commit()
        conexao.close()


while True:

    print('----X Menu X----\n'
          '1 - Inserir Dados\n'
          '2 - Visualizar Dados\n'
          '3 - Excluir Dados\n'
          '4 - Sair\n')

    opcoes = int(input('Digite Uma Opção: '))
    try:
        if opcoes == 1:
            colocar_dados()

        if opcoes == 2:
            exibir_dados()

        if opcoes == 3:
            excluir_dados()

        elif opcoes == 4:
            print('Fim do Programa!!!')
            break

    except ValueError:
        print('Digite uma Valor Válido!!!')