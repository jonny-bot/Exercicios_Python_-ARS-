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


def conectar():
    conexao = sqlite3.connect('meu_banco.db')
    cursor = conexao.cursor()
    return conexao, cursor


def criar_banco():
    with sqlite3.connect('meu_banco.db') as conexao:
        cursor = conexao.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS produtos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                codigo TEXT NOT NULL UNIQUE,
                descricao TEXT NOT NULL,
                quantidade INTEGER NOT NULL,
                preco REAL NOT NULL
            )''')
        print('Banco Criado!!!')


def inserir_dados(codigo, descricao, quantidade, preco):
    conexao, cursor =  conectar()

    cursor.execute(''' INSERT INTO produtos (codigo, descricao, quantidade, preco) 
    VALUES (?, ?, ?, ?) ''', (codigo, descricao, quantidade, preco))

    conexao.commit()
    conexao.close()


def mostrar_dados():
    conexao, cursor =  conectar()

    cursor.execute(''' SELECT * FROM produtos ''')

    for i in cursor.fetchall():
        print(f"ID: {i[0]} || CODIGO: {i[1]} || DESCRICAO: {i[2]} || QUANTIDADE: {i[3]} || PRECO: {i[4]}")


def consulta_espefica():
    conexao, cursor =  conectar()

    quantidade_produto = int(input('Qual a Quantidade de Produto: '))

    cursor.execute("SELECT id, descricao, quantidade FROM produtos WHERE quantidade > ?", (quantidade_produto,))

    resultados = cursor.fetchall()
    contagem_produto = 0
    for id, descricao, quantidade in resultados:
        contagem_produto += 1
        print(f"{contagem_produto}. ID: {id} || Produto {descricao} com {quantidade} em estoque.")

    conexao.close()


def excluir():
    conexao, cursor =  conectar()

    print('1 - Excluir uma Unidade || 2 - Excluir Toda a Tabela')
    opcao = int(input('Digite uma das Opçoes: '))

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


criar_banco()


while True:
    print('Selecione... 1 - Inserir Dados || 2 - Mostrar Dados || 3 - Excluir || 4 - Mostrar Dados || 5 - Sair')

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
        excluir()

    elif opcao == 4:
        consulta_espefica()

    elif opcao == 5:
        print('Fim do Programa!!!')
        break