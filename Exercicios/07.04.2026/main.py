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
        CREATE TABLE IF NOT EXISTS conta_bancaria (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_conta TEXT NOT NULL UNIQUE,
            senha_conta TEXT NOT NULL,
            saldo_conta REAL NOT NULL DEFAULT 0.0
        )
    ''')

    conexao.commit()
    conexao.close()


def criar_conta(nome_conta, senha_conta):
    conexao, cursor = conexao_cursor()

    cursor.execute("INSERT INTO conta_bancaria (nome_conta, senha_conta) "
                   "VALUES (?, ?)", (nome_conta, senha_conta))

    print('Conta Criada Com Sucesso!!!')

    conexao.commit()
    conexao.close()


def autenticar_conta(nome_conta, senha_conta):
    conexao, cursor = conexao_cursor()

    cursor.execute("SELECT * FROM conta_bancaria WHERE nome_conta = ? AND senha_conta = ?",
                   (nome_conta, senha_conta))

    resultado = cursor.fetchone()

    conexao.close()

    return resultado is not None


def deletar_conta(nome_conta, senha_conta):
    conexao, cursor = conexao_cursor()

    cursor.execute(
        "DELETE FROM conta_bancaria WHERE nome_conta = ? AND senha_conta = ?",
        (nome_conta, senha_conta)
    )

    if cursor.rowcount > 0:
        print('Conta excluída com sucesso!')

    else:
        print('Nenhuma conta encontrada com esses dados.')

    conexao.commit()
    conexao.close()


def fazer_deposito(nome_conta, valor_depositado):
    conexao, cursor = conexao_cursor()

    cursor.execute("SELECT saldo_conta FROM conta_bancaria WHERE nome_conta = ?", (nome_conta,))
    resultado = cursor.fetchone()

    if resultado:
        saldo_atual = resultado[0]
        novo_saldo = saldo_atual + valor_depositado

        cursor.execute("UPDATE conta_bancaria SET saldo_conta = ? WHERE nome_conta = ?",
                       (novo_saldo, nome_conta))

        print(f'Depósito de {valor_depositado:.2f} realizado com sucesso! Novo saldo: {novo_saldo:.2f}')

    else:
        print("Conta não encontrada.")

    conexao.commit()
    conexao.close()


def fazer_saque(nome_conta, valor_saque):
    conexao, cursor = conexao_cursor()

    try:
        cursor.execute("SELECT saldo_conta FROM conta_bancaria WHERE nome_conta = ?", (nome_conta,))
        resultado = cursor.fetchone()

        if resultado:
            saldo_atual = resultado[0]

            if saldo_atual >= valor_saque:
                novo_saldo = saldo_atual - valor_saque

                cursor.execute("UPDATE conta_bancaria SET saldo_conta = ? WHERE nome_conta = ?",
                               (novo_saldo, nome_conta))

                print(f'Saque de {valor_saque:.2f} realizado com sucesso! Novo saldo: {novo_saldo:.2f}')

            else:
                print("Saldo insuficiente para realizar o saque.")

        else:
            print("Conta não encontrada.")

        conexao.commit()

    except Exception as e:
        print(f"Erro ao realizar saque: {e}")

    finally:
        conexao.close()


def fazer_transferencia(conta_origem, conta_destino, valor_transferencia):
    conexao, cursor = conexao_cursor()

    try:
        # Verifica saldo da conta de origem
        cursor.execute("SELECT saldo_conta FROM conta_bancaria WHERE nome_conta = ?", (conta_origem,))
        resultado_origem = cursor.fetchone()

        # Verifica existência da conta de destino
        cursor.execute("SELECT saldo_conta FROM conta_bancaria WHERE nome_conta = ?", (conta_destino,))
        resultado_destino = cursor.fetchone()

        if not resultado_origem:
            print("Conta de origem não encontrada.")
            return

        if not resultado_destino:
            print("Conta de destino não encontrada.")
            return

        saldo_origem = resultado_origem[0]

        saldo_destino = resultado_destino[0]

        if saldo_origem >= valor_transferencia:
            novo_saldo_origem = saldo_origem - valor_transferencia
            novo_saldo_destino = saldo_destino + valor_transferencia

            # Atualiza saldo das duas contas
            cursor.execute("UPDATE conta_bancaria SET saldo_conta = ? WHERE nome_conta = ?",
                           (novo_saldo_origem, conta_origem))

            cursor.execute("UPDATE conta_bancaria SET saldo_conta = ? WHERE nome_conta = ?",
                           (novo_saldo_destino, conta_destino))

            print(f'Transferência de {valor_transferencia:.2f} realizada com sucesso!\n'
                  f'Novo saldo da conta {conta_origem}: {novo_saldo_origem:.2f}\n'
                  f'Novo saldo da conta {conta_destino}: {novo_saldo_destino:.2f}')

        else:
            print("Saldo insuficiente para realizar a transferência.")

        conexao.commit()

    except Exception as e:

        print(f"Erro ao realizar transferência: {e}")
        conexao.rollback()

    finally:
        conexao.close()


criar_tabela()

try:
    
    lista_opcao = ['Sair do Programa',
                   'Criar Conta',
                   'Fazer Login',
                   'Excluir Conta']

    while True:

        for contador, lista in enumerate(lista_opcao):
            print(f'{contador} - {lista}')

        opcao = int(input('Digite Uma das Opções: '))

        match opcao:
            case 0:
                print('Saindo do Programa...')
                break

            case 1:
                nome_conta = input('Digite o Nome da Conta: ')
                senha_conta = input('Digite a Senha da Conta: ')
                criar_conta(nome_conta, senha_conta)

            case 2:
                login_conta = input('Digite o Nome da Conta: ')
                senha_conta = input('Digite a Senha da Conta: ')

                if autenticar_conta(login_conta, senha_conta):
                    print(f'Seja Bem Vindo {login_conta}.')

                    lista_operacoes = ['Sair da Conta',
                                       'Realizar Deposito',
                                       'Realizar Saque',
                                       'Realizar Transferencias']

                    while True:
                        for contador, lista in enumerate(lista_operacoes):
                            print(f'{contador} - {lista}')

                        try:
                            tipo_operacao = int(input('Digite uma das Operações: '))

                            match tipo_operacao:
                                case 0:
                                    print('Fim da Operação...')
                                    break

                                case 1:
                                    valor_depositado = float(input('Digite o Valor a Ser Depositado: '))
                                    fazer_deposito(login_conta, valor_depositado)

                                case 2:
                                    valor_saque = float(input('Digite o Valor a Ser Sacado: '))
                                    fazer_saque(login_conta, valor_saque)

                                case 3:
                                    conta_destino = input('Digite a Conta para a Transferencia: ')
                                    valor_transferencia = float(input('Digite o Valor a Ser Transferido: '))
                                    fazer_transferencia(login_conta, conta_destino, valor_transferencia)

                                case _:
                                    print(f'Opção inválida.')

                        except ValueError:
                            print('Digite uma Entrada Válida!!!')

                else:
                    print("Login inválido. Tente novamente.")

            case 3:
                nome_conta = input('Digite o Nome da Conta: ')
                senha_conta = input('Digite a Senha da Conta: ')
                deletar_conta(nome_conta, senha_conta)

            case _:
                print(f'Opção inválida.')

except ValueError:
    print('Digite uma Entrada Válida!!!')
