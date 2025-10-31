import sqlite3
import random


def gerar_codigo():

    codigo = random.randint(1000, 9999)
    return codigo


def gerar_descricao():
    lista = [
    "Cimento", "Areia", "Brita", "Tijolo", "Bloco de concreto", "Cal hidratada", "Argamassa", "Ferro para construção",
    "Viga de aço", "Telha cerâmica", "Telha de fibrocimento", "Tinta acrílica", "Primer", "Verniz", "Canos de PVC",
    "Joelhos e conexões", "Fita veda rosca", "Caixa d'água", "Porta de madeira", "Janela de alumínio", "Martelo",
    "Chave de fenda", "Alicate", "Serrote", "Trena", "Nível de bolha", "Furadeira", "Parafusadeira", "Marreta",
    "Esquadro", "Desempenadeira", "Colher de pedreiro", "Lixadeira", "Plaina elétrica", "Escada", "Carrinho de mão",
    "Betoneira", "Lanterna", "Capacete de segurança", "Óculos de proteção"]

    escolher_lista = random.choice(lista)

    return escolher_lista


def gerar_quantidade():
    codigo = random.randint(1, 200)
    return codigo


def gerar_preco():
    codigo = round(random.uniform(10.00, 99.99), 2)
    return codigo


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


def inserir_dados(codigo, descricao, quantidade, preco):
    conexao = sqlite3.connect('meu_banco.db')
    cursor = conexao.cursor()

    cursor.execute(''' INSERT INTO produtos (codigo, descricao, quantidade, preco) 
    VALUES (?, ?, ?, ?) ''', (codigo, descricao, quantidade, preco))

    conexao.commit()
    conexao.close()


def mostrar_dados():
    conexao = sqlite3.connect('meu_banco.db')
    cursor = conexao.cursor()

    cursor.execute(''' SELECT * FROM produtos ''')

    for i in cursor.fetchall():
        print(f"ID: {i[0]} || CODIGO: {i[1]} || DESCRICAO: {i[2]} || QUANTIDADE: {i[3]} || PRECO: {i[4]}")

    conexao.close()


def consulta_id(id):
    conexao = sqlite3.connect('meu_banco.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM produtos WHERE id = ?", (id,))

    resultados = cursor.fetchall()
    for i in resultados:
        print(f"ID: {i[0]} || CODIGO: {i[1]} || DESCRICAO: {i[2]} || QUANTIDADE: {i[3]} || PRECO: {i[4]}")

    conexao.close()


def consulta_codigo(codigo):
    conexao = sqlite3.connect('meu_banco.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM produtos WHERE codigo = ?", (codigo,))

    resultados = cursor.fetchall()
    for i in resultados:
        print(f"ID: {i[0]} || CODIGO: {i[1]} || DESCRICAO: {i[2]} || QUANTIDADE: {i[3]} || PRECO: {i[4]}")

    conexao.close()


def consulta_descricao(descricao):
    conexao = sqlite3.connect('meu_banco.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM produtos WHERE descricao = ?", (descricao,))

    resultados = cursor.fetchall()
    for i in resultados:
        print(f"ID: {i[0]} || CODIGO: {i[1]} || DESCRICAO: {i[2]} || QUANTIDADE: {i[3]} || PRECO: {i[4]}")

    conexao.close()


def consulta_preco(opcao):
    conexao = sqlite3.connect('meu_banco.db')
    cursor = conexao.cursor()

    if opcao == 1:

        preco_1 = float(input('Qual o Preço que você busca: '))

        cursor.execute("SELECT * FROM produtos WHERE preco = ?", (preco_1,))

        resultados = cursor.fetchall()
        for i in resultados:
            print(f"ID: {i[0]} || CODIGO: {i[1]} || DESCRICAO: {i[2]} || QUANTIDADE: {i[3]} || PRECO: {i[4]}")

    elif opcao == 2:

        preco_2 = float(input('Qual o Preço que você busca Acima de: '))

        cursor.execute("SELECT * FROM produtos WHERE preco > ?", (preco_2,))

        resultados = cursor.fetchall()
        for i in resultados:
            print(f"ID: {i[0]} || CODIGO: {i[1]} || DESCRICAO: {i[2]} || QUANTIDADE: {i[3]} || PRECO: {i[4]}")

    elif opcao == 2:

        preco_3 = float(input('Qual o Preço que você busca Acima de: '))

        cursor.execute("SELECT * FROM produtos WHERE preco < ?", (preco_3,))

        resultados = cursor.fetchall()
        for i in resultados:
            print(f"ID: {i[0]} || CODIGO: {i[1]} || DESCRICAO: {i[2]} || QUANTIDADE: {i[3]} || PRECO: {i[4]}")

    conexao.close()


def excluir(opcao):
    conexao = sqlite3.connect('meu_banco.db')
    cursor = conexao.cursor()

    if opcao == 1:
        id = int(input('Digite ao ID você quer Excluir: '))

        cursor.execute("DELETE FROM produtos WHERE id = ?", (id,))
        print('Excluido com Sucesso!!!')

        conexao.commit()
        conexao.close()

    elif opcao == 2:

        cursor.execute("DELETE FROM produtos")

        cursor.execute("DELETE FROM sqlite_sequence WHERE name='produtos'")

        print('Excluido com Sucesso!!!')

        conexao.commit()
        conexao.close()


def atualizar_descricao(codigo, descricao):
    conexao = sqlite3.connect('meu_banco.db')
    cursor = conexao.cursor()

    cursor.execute("UPDATE produtos "
                   "SET descricao=? "
                   "WHERE codigo=?",
                   (descricao,codigo))

    if cursor.rowcount == 0:
        print('Código não existe!!!')
    else:
        conexao.commit()
        print('Alterado com Sucesso!!!')

        conexao.close()


def atualizar_quantidade(codigo, quantidade):
    conexao = sqlite3.connect('meu_banco.db')
    cursor = conexao.cursor()

    cursor.execute("UPDATE produtos "
                   "SET quantidade=? "
                   "WHERE codigo=? ",
                   (quantidade, codigo))

    if cursor.rowcount == 0:
        print('Código não existe!!!')
    else:
        conexao.commit()
        print('Alterado com Sucesso!!!')

        conexao.close()


def atualizar_preco(codigo, preco):
    conexao = sqlite3.connect('meu_banco.db')
    cursor = conexao.cursor()

    cursor.execute("UPDATE produtos "
                   "SET preco=? "
                   "WHERE codigo=? ",
                   (preco, codigo))

    if cursor.rowcount == 0:
        print('Código não existe!!!')
    else:
        conexao.commit()
        print('Alterado com Sucesso!!!')

        conexao.close()


def verificar_existencia(codigo):
    conexao = sqlite3.connect('meu_banco.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM produtos WHERE codigo = ?", (codigo,))
    resultado = cursor.fetchall()

    for i in resultado:
        print(f"ID: {i[0]} || CODIGO: {i[1]} || DESCRICAO: {i[2]} || QUANTIDADE: {i[3]} || PRECO: {i[4]}")

    conexao.close()

    if resultado:
        return True
    else:
        return False



criar_banco()


while True:
    print('----X Menu X----\n'
          '1 - Inserir Dados\n'
          '2 - Mostrar Dados\n'
          '3 - Excluir\n'
          '4 - Consulta ID\n'
          '5 - Consulta Código\n'
          '6 - Consulta Descrição\n'
          '7 - Consulta Preço\n'
          '8 - Atualizar\n'
          '9 - Sair')

    opcao = int(input('Digite a Opção: '))

    if opcao == 1:

        contagem = 1

        total = int(input('Vamos Gerar Quantos Dados: '))

        while contagem < (total + 1):
            codigo = gerar_codigo()
            descricao = gerar_descricao()
            quantidade = gerar_quantidade()
            preco = gerar_preco()

            contagem += 1

            inserir_dados(codigo, descricao, quantidade, preco)
        print('Dados Adicionados com Sucesso!!!')

    elif opcao == 2:
        mostrar_dados()

    elif opcao == 3:
        print('1 - Excluir uma Unidade || 2 - Excluir Toda a Tabela')
        opcao = int(input('Digite uma das Opçoes: '))
        excluir(f'{opcao}')

    elif opcao == 4:
        id = int(input('Qual o Código do Produto: '))
        consulta_id(f'{id}')

    elif opcao == 5:
        codigo = input('Digite o Código: ')
        consulta_codigo(f'{codigo}')

    elif opcao == 6:
        descricao = input('Qual o Nome do Produto: ')
        consulta_descricao(f'{descricao}')

    elif opcao == 7:
        print('1 - Buscar Preço Unico || 2 - Buscar Preços acima de || 3 - Buscar Preços a Baixo de')
        opcao = int(input('Digite umas das Opções: '))
        consulta_preco(f'{opcao}')

    elif opcao == 9:
        print('Fim do Programa!!!')
        break

    elif opcao == 8:

        codigo = str(input('Qual o Código do Produto: '))

        if verificar_existencia(f"{codigo}"):
            consulta_descricao(f'{codigo}')

            print('Para Atualizar: 1 - Descrição || 2 - Quantidade || 3 - Preço')

            tipo_atualizar = int(input('Digite uma Opção: '))

            if tipo_atualizar == 1:

                descricao = input('Qual a Descricao do Produto: ')

                atualizar_descricao(codigo, descricao)

            elif tipo_atualizar == 2:

                quantidade = int(input('Qual a Quantidade do Produto: '))

                atualizar_quantidade(codigo, quantidade)

            elif tipo_atualizar == 3:

                preco = float(input('Qual o Preço: '))

                atualizar_preco(codigo, preco)

        else:
            print('Código Não Consta!!!')