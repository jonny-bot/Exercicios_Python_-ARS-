import random
import sqlite3


def gerar_codigo():
    return random.randint(1000,9999)


def gerar_descricao():
    lista = ["Cimento", "Areia", "Pedra brita", "Tijolo", "Bloco de concreto", "Cal", "Gesso",
             "Argamassa", "Madeira", "Telha", "Ferro", "Aço", "Vidro", "Cerâmica", "PVC", "Tinta",
             "Verniz", "Plástico", "Isopor", "Drywall", "Cobertura metálica", "Tubo galvanizado",
             "Concreto armado", "Rejunte", "Piso laminado", "Mármore", "Granito", "Louça sanitária",
             "Impermeabilizante", "Fita veda rosca", "Parafuso", "Prego", "Cola de contato", "Silicone",
             "Lã de vidro", "Placa OSB", "Fibrocimento", "Esquadria de alumínio", "Placa cimentícia",
             "Papelão ondulado"]

    return random.choice(lista)


def gerar_preco():
    valor = random.uniform(59.99, 999.99)
    float(f'{valor:.2f}')
    return valor


def gerar_quantidade():
    return random.randint(50, 500)


def criar_tabela():
    conexao = sqlite3.connect("meu_banco.db")
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        codigo TEXT NOT NULL,
        descricao TEXT NOT NULL,
        preco REAL NOT NULL,
        quantidade INTEGER NOT NULL
    );
    """)

    print("Tabela criada com sucesso!")

    conexao.commit()
    conexao.close()


def inserir_dados(codigo, descricao, preco, quantidade):
    conexao = sqlite3.connect("meu_banco.db")
    cursor = conexao.cursor()

    cursor.execute(''' INSERT INTO produtos (codigo, descricao, preco, quantidade)
    VALUES (?, ?, ?, ?) ''', (codigo, descricao, preco, quantidade))

    conexao.commit()
    conexao.close()


def mostrar_dados():
    conexao = sqlite3.connect("meu_banco.db")
    cursor = conexao.cursor()

    while True:
        try:

            opcao = int(input('0 - Sair do Programa...\n'
                              '1 - Mostrar Todos os Dados\n'
                              '2 - Mostrar Preço Maior que um valor\n'
                              '3 - Mostrar Preço Menor que um valor\n'
                              '4 - Mostrar Preço entre dois valores\n'
                              '5 - Mostrar por Código\n'
                              'Digite umas das Opções: '))

            if 0 <= opcao <= 5:

                if opcao == 0:
                    print('Saindo...')
                    break

                elif opcao == 1:

                    cursor.execute(''' SELECT * FROM produtos ''')

                    resultado = cursor.fetchall()

                    for dados in resultado:
                        print(f"ID: {dados[0]} || CODIGO: {dados[1]} || DESCRICAO: {dados[2]} || "
                              f"PREÇO: {dados[3]:.2f} || QUANTIDADE: {dados[4]}")

                elif opcao == 2:

                    valor = int(input('Digite o Valor: '))

                    cursor.execute(f"SELECT * FROM produtos WHERE preco > {valor}")

                    resultado = cursor.fetchall()

                    for maior in resultado:
                        print(maior)

                elif opcao == 3:

                    valor = int(input('Digite o Valor: '))

                    cursor.execute(f"SELECT * FROM produtos WHERE preco < {valor}")

                    resultado = cursor.fetchall()

                    for menor in resultado:
                        print(menor)

                elif opcao == 4:

                    entre = int(input('Entre: '))

                    ate = int(input('Até: '))

                    if ate < entre:

                        print('Você Precisa Colocar um Número Maior.')

                    else:

                        cursor.execute(f"SELECT * FROM produtos WHERE preco BETWEEN {entre} AND {ate}")

                        resultado = cursor.fetchall()

                        for entre_dois in resultado:
                            print(entre_dois)

                elif opcao == 5:

                    codigo_procurado = input("Digite o código do produto: ")

                    cursor.execute('''SELECT * FROM produtos WHERE codigo = ?''', (codigo_procurado,))

                    resultado = cursor.fetchall()

                    if resultado:

                        for dados in resultado:
                            print(
                                f"ID: {dados[0]} || CODIGO: {dados[1]} || DESCRICAO: {dados[2]} || "
                                f"PREÇO: {dados[3]:.2f} || QUANTIDADE: {dados[4]}")

                    else:
                        print("Dado não existe na tabela.")

            else:
                print(f'Você Digitou {opcao}. Que não está Entre 0 e 5.')

        except ValueError:
            print('Digite uma Entrada Válida!')


def excluir_dados():
    conexao = sqlite3.connect("meu_banco.db")
    cursor = conexao.cursor()

    while True:
        try:

            opcao = int(input("0 - Sair\n"
                              "1 - Excluir tudo\n"
                              "2 - Excluir por ID\n"
                              "3 - Excluir por Código\n"
                              "Digite umas das Opções: "))

            if opcao == 0:
                print("Saindo...")
                break

            elif opcao == 1:

                confirmacao = int(input("0 - SAIR || 1 - SIM || 2 - NÃO\nVocê realmente quer excluir todos os dados? "))

                if confirmacao == 0:
                    print("Saindo...")

                elif confirmacao == 1:

                    cursor.execute("DELETE FROM produtos;")

                    cursor.execute("DELETE FROM sqlite_sequence WHERE name='produtos';")

                    print("Todos os dados foram apagados com sucesso!")

                elif confirmacao == 2:
                    print("Nenhum dado apagado!")

                else:
                    print(f"Você digitou {confirmacao}, que não está entre 0 e 2.")

            elif opcao == 2:

                try:
                    id_deletado = int(input("Digite o ID a ser deletado: "))

                    cursor.execute("DELETE FROM produtos WHERE id = ?", (id_deletado,))

                    print("Produto deletado com sucesso!")

                except ValueError:
                    print("Digite um número válido para o ID.")

            elif opcao == 3:

                try:
                    codigo_deletado = int(input("Digite o Código a ser deletado: "))

                    cursor.execute("DELETE FROM produtos WHERE codigo = ?", (codigo_deletado,))

                    print("Produto deletado com sucesso!")

                except ValueError:
                    print("Digite um número válido para o Código.")

            else:
                print(f"Você digitou {opcao}, que não está entre 0 e 3.")

            conexao.commit()

        except ValueError:
            print("Digite uma entrada válida!")


    conexao.close()


def atualizar_dados():
    conexao = sqlite3.connect("meu_banco.db")
    cursor = conexao.cursor()

    alterar_codigo = input('Digite o Código do Produto: ')

    cursor.execute('''SELECT * FROM produtos WHERE codigo = ?''', (alterar_codigo,))

    resultado = cursor.fetchall()

    if resultado:

        for dados in resultado:
            print(
                f"ID: {dados[0]} || CODIGO: {dados[1]} || DESCRICAO: {dados[2]} || "
                f"PREÇO: {dados[3]:.2f} || QUANTIDADE: {dados[4]}")

    else:
        print("O Dado não encontrado na tabela.")


    while True:
        try:

            opcao = int(input('0 - Sair...\n'
                              '1 - Atualizar Descrição\n'
                              '2 - Atualizar Preço\n'
                              '3 - Atualizar Quantidade\n'
                              'Digite umas das Opções: '))

            if 0 <= opcao <= 3:

                if opcao == 0:
                    print('Saindo...')
                    break

                elif opcao == 1:

                    alterar_descricao = input('Digite o Nome a ser Alterado: ')

                    cursor.execute("UPDATE produtos SET descricao = ? WHERE codigo = ?",
                                   (alterar_descricao, alterar_codigo))

                    print('Alteração Realizada com Sucesso!')

                elif opcao == 2:

                    alterar_preco = float(input('Digite a Novo Preço: '))

                    cursor.execute("UPDATE produtos SET preco = ? WHERE codigo = ?",
                                   (alterar_preco, alterar_codigo))

                    print('Alteração Realizada com Sucesso!')

                elif opcao == 3:

                    alterar_quantidade = int(input('Digite a Nova Quantidade: '))

                    cursor.execute("UPDATE produtos SET quantidade = ? WHERE codigo = ?",
                                           (alterar_quantidade, alterar_codigo))

                    print('Alteração Realizada com Sucesso!')

                conexao.commit()

                cursor.execute('''SELECT * FROM produtos WHERE codigo = ?''', (alterar_codigo,))

                resultado = cursor.fetchall()

                for atualizacao_dados in resultado:
                    print(f"ID: {atualizacao_dados[0]} || CODIGO: {atualizacao_dados[1]} || DESCRICAO: {atualizacao_dados[2]} || "
                          f"PREÇO: {atualizacao_dados[3]:.2f} || QUANTIDADE: {atualizacao_dados[4]}")

            else:
                print(f'Você Digitou {opcao}. Que não está entre 0 e 3.')

        except ValueError:
            print('Digite uma Entrada Válida!')

    conexao.close()


criar_tabela()


while True:
    try:

        opcao = int(input('0 - Sair do Programa!\n'
                          '1 - Inserir Dados na Tabela\n'
                          '2 - Mostrar Dados na Tabela\n'
                          '3 - Excluir Dados na Tabela\n'
                          '4 - Atualizar Dados Na Tabela\n'
                          'Digite umas das Opções: '))

        if 0 <= opcao <= 4:

            if opcao == 0:
                print('Saindo do Programa...')
                break

            elif opcao == 1:

                total_dados = int(input('Digite o Total de Dados a ser Gerados: '))

                for i in range(total_dados):
                    codigo = gerar_codigo()
                    descricao = gerar_descricao()
                    preco = gerar_preco()
                    quantidade = gerar_quantidade()

                    inserir_dados(codigo, descricao, preco, quantidade)

                print('Todos os Dados Gerados com Sucesso...')

            elif opcao == 2:
                mostrar_dados()

            elif opcao == 3:
                excluir_dados()

            elif opcao == 4:
                atualizar_dados()

        else:
            print(f'Você Digitou {opcao}. Que não está entre 0 e 3.')

    except ValueError:
        print('Digite uma Entrada Válida!')
