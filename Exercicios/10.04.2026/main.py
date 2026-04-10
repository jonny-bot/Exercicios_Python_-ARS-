import sqlite3


# Conectar ao banco de dados (ou criar se não existir)
def conectar_banco():

    conexao = sqlite3.connect("atm.db")
    cursor = conexao.cursor()

    return conexao, cursor


# Criar tabela de contas
def criar_tabela():
    conexao, cursor = conectar_banco()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_conta TEXT NOT NULL,
            senha_conta TEXT NOT NULL,
            saldo_conta REAL NOT NULL
        )
    """)


def listar_login():
    listar_login = ['Saindo do Programa',
                    'Criar Conta',
                    'Realizar Login',
                    'Excluir Conta',
                    'Listar Contas']

    for contador, lista in enumerate(listar_login):
        print(f'{contador} - {lista}')


def listar_operacoes():
    listar_operacoes = ['Sair da Conta',
                        'Realizar Deposito',
                        'Realizar Saque',
                        'Realizar Tranferência',
                        'Consultar Saldo Atual',
                        'Alterar Senha']

    for contador, lista in enumerate(listar_operacoes):
        print(f'{contador} - {lista}')


# Funções CRUD
def criar_conta(nome_conta,  senha_conta, saldo_conta):
    conexao, cursor = conectar_banco()

    cursor.execute("INSERT INTO contas (nome_conta, senha_conta,saldo_conta) "
                   "VALUES (?, ?, ?)", (nome_conta, senha_conta,saldo_conta))

    conexao.commit()

    # Fechar conexão
    conexao.close()

    print("Conta criada com sucesso!")


def ler_contas():
    conexao, cursor = conectar_banco()

    cursor.execute("SELECT * FROM contas")

    for conta in cursor.fetchall():
        print(conta)


def atualizar_saldo(nome_conta, novo_saldo):
    conexao, cursor = conectar_banco()

    cursor.execute("UPDATE contas SET saldo = ? WHERE nome_conta = ?", (novo_saldo, nome_conta))

    conexao.commit()

    # Fechar conexão
    conexao.close()

    print("Saldo atualizado!")


def deletar_conta(nome_conta):
    conexao, cursor = conectar_banco()

    cursor.execute("DELETE FROM contas WHERE nome_conta = ?", (nome_conta,))

    conexao.commit()

    # Fechar conexão
    conexao.close()

    print("Conta deletada!")


# Exemplo de uso
while True:
    try:

        login = listar_login()

        print(login)

        tela_inicial = int(input('Digite Uma das Opções: '))

        match tela_inicial:

            case 0:
                print('Fim do Programa...')
                break

            case 1:
                nome_conta = input('Digite o Nome da Conta: ')
                senha_conta = input('Digite a Senha da Conta: ')
                saldo_conta = float(input('Digite o Saldo da Conta: '))
                criar_conta(nome_conta, senha_conta, saldo_conta)

            case 2:
                operacoes = listar_operacoes()

                print(operacoes)

                operacao = input('Digite uma das Operações: ')
                print(f'Operação escolhida: {operacao}')

            case 3:
                nome_conta = input('Digite o Nome da Conta a ser Excluída: ')
                deletar_conta(nome_conta)

            case 4:
                ler_contas()

            case _:
                print('Opção inválida!')

    except ValueError:
        print('Digite uma Entrada Válida!!!')
