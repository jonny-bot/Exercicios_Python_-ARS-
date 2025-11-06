import sqlite3


#  Criar Usuários (✅)
def criar_banco_usuarios():
    conexao = sqlite3.connect('conta_bancaria.db')
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS conta_bancaria(
            id INTEGER PRIMARY KEY AUTOINCREMENT,  
            nome TEXT NOT NULL UNIQUE,           
            senha TEXT NOT NULL,         
            saldo REAL NOT NULL,
            contador INTEGER NOT NULL,
            bloqueador TEXT NOT NULL
        )''')

    conexao.commit()
    conexao.close()


#  Criar Conta (✅)
def criar_contas(criar_nome, criar_senha, criar_saldo):
    conexao = sqlite3.connect('conta_bancaria.db')
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO conta_bancaria (nome, senha, saldo, contador, bloqueador) "
                   "VALUES (?, ?, ?, ?, ?)", (criar_nome, criar_senha, criar_saldo, 0 , 'N'))

    print('Conta Criado com Sucesso!!!')

    conexao.commit()
    conexao.close()


#  Autenticar Usuários (✅)
def autenticar_usuarios(autenticar_nome, autenticar_senha):
    conexao = sqlite3.connect('conta_bancaria.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM conta_bancaria WHERE nome = ? AND senha = ?", (autenticar_nome, autenticar_senha))

    resultado = cursor.fetchone()

    conexao.close()

    if resultado:
        print('Usuário Autenticado com Sucesso!')
        return True
    else:
        print('Usuário ou Senha Incorretos!')

        conexao = sqlite3.connect('conta_bancaria.db')
        cursor = conexao.cursor()

        cursor.execute("SELECT contador FROM conta_bancaria WHERE nome = ?", (autenticar_nome, ))

        contador = cursor.fetchall()

        num = contador[0]
        print(num)


        return False


#  Realizar Saques (✅)
def fazer_saques(saque_nome):
    conexao = sqlite3.connect('conta_bancaria.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM conta_bancaria WHERE nome = ?", (saque_nome,))
    resultado = cursor.fetchone()

    if resultado:
        saldo_atual  = resultado[3]
        print(f'O seu Saldo Atual é: R${saldo_atual:.2f}')

        valor_saque = float(input('Você Vai Sacar: R$'))

        if valor_saque <= saldo_atual:
            novo_saldo = saldo_atual - valor_saque

            cursor.execute("UPDATE conta_bancaria SET saldo = ? WHERE nome = ?", (novo_saldo, saque_nome))
            conexao.commit()

            notas_retiradas = retira_notas(valor_saque)
            print("Notas retiradas:")

            for nota, quantidade in notas_retiradas.items():
                print(f"{quantidade} nota(s) de R${nota}")

            print(f"Saque de R${valor_saque:.2f} realizado com sucesso.\n"
                  f"Seu Saldo Atual: R${novo_saldo}")
        else:
            print("Saldo insuficiente para o saque.")
    else:
        print("Usuário não encontrado.")

    conexao.close()


#  Notas Geradas (✅)
def retira_notas(valor_saque):
    notas = [100, 50, 20, 10, 5]
    resultado = {}

    for i in notas:
        quantidade = valor_saque // i

        if quantidade > 0:
            resultado[i] = quantidade
            valor_saque -= quantidade * i

    return resultado


#  Realizar Deposito (✅)
def fazer_deposito(deposito_nome):
    conexao = sqlite3.connect('conta_bancaria.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM conta_bancaria WHERE nome = ?", (deposito_nome, ))
    resultado = cursor.fetchone()

    if resultado:
        saldo_atual  = resultado[3]
        print(f'O seu Saldo Atual é: R${saldo_atual:.2f}')

        depositar = float(input('Voçê quer Depositar Quanto: '))
        novo_saldo = saldo_atual + depositar

        cursor.execute("UPDATE conta_bancaria SET saldo = ? WHERE nome = ?", (novo_saldo, deposito_nome))
        conexao.commit()

        print(f"Saque de R${depositar:.2f} realizado com sucesso.\n"
              f"Seu Saldo Atual é de: {novo_saldo}")

    conexao.close()


#  Deletar Usuário (✅)
def deletar_usuario(delete_nome, delete_senha):
    conexao = sqlite3.connect('conta_bancaria.db')
    cursor = conexao.cursor()

    while True:
        try:
            confirmacao = int(input('Você Deseja Apagar a Conta? \n1 - Sim || 2 - Não\n'))

            if confirmacao == 1:

                cursor.execute("DELETE FROM conta_bancaria WHERE nome = ? AND senha = ?", (delete_nome, delete_senha))
                conexao.commit()

                if cursor.rowcount > 0:
                    print('Usuário Deletado com Sucesso!!!')
                    conexao.close()
                    return True
                else:
                    print('Usuário ou Senha Incorretos!')
                    conexao.close()
                    return False

            elif confirmacao == 2:
                print('Operação Cancelada!!!')
                conexao.close()
                break

        except ValueError:
            print('Digite Uma Entrada Válida!!!')


#  Deletar Todos os Dados (✅)
def deletar_tabela():
    conexao = sqlite3.connect('conta_bancaria.db')
    cursor = conexao.cursor()

    while True:
        confirmacao = int(input('Você Deseja Apagar todas as Conta? \n1 - Sim || 2 - Não\n'))
        try:
            if confirmacao == 1:

                cursor.execute("DELETE FROM sqlite_sequence WHERE name='conta_bancaria'")

                conexao.commit()
                conexao.close()

                print('Contas Excluídas com Sucesso!!!')
                break

            elif confirmacao == 2:
                print('Operação Cancelada!!!')
                conexao.close()
                break

        except ValueError:
            print('Digite Uma Entrada Valida!!!')


criar_banco_usuarios()


while True:
    try:
        print('1 - Criar Conta\n'
              '2 - Deletar Usuário\n'
              '3 - Autenticar Usuários\n'
              '4 - Realizar Saques\n'
              '5 - Realizar Deposito\n'
              '0 - Sair do Programa')

        opcoes = int(input('Digite Umas Das Opções: '))

        if opcoes == 0:
            print('Fim do Programa!!!')
            break

        if opcoes == 1:
            criar_nome = input('Digite o Nome da Conta: ')
            criar_senha = input('Digite a Senha da Conta: ')
            criar_saldo = float(input('Digite o Saldo Inicial da Conta: '))
            criar_contas(criar_nome, criar_senha, criar_saldo)

        if opcoes == 2:
            opcao = int(input('1 - Deletar Conta Especifica || 2 - Deletar Todas as Contas\n'))

            if opcao == 1:
                delete_nome = input('Digite o Nome da Conta: ')
                delete_senha = input('Digite a Senha para Excluir: ')
                deletar_usuario(delete_nome, delete_senha)

            if opcao == 2:
                deletar_tabela()

        if opcoes == 3:

            tentativas = 0

            while tentativas < 3:

                if tentativas < 3:

                    autenticar_nome = input('Digite o Nome da Conta Para Autenticar: ')
                    autenticar_senha = input('Digite a Senha da Conta Para Autenticar: ')

                    autenticar_usuarios(autenticar_nome, autenticar_senha)
                    break

                elif tentativas < 1:
                    print('Tente Novamente!!!')
                    tentativas += 1

                else:
                    print('Usuário Bloqueado!!!')

        if opcoes == 4:
            saque_nome = input('Digite o Nome da Conta para Realizar o Saque: ')
            fazer_saques(saque_nome)

        if opcoes == 5:
            deposito_nome = input('Digite o Nome da Conta para Realizar o Deposito: ')
            fazer_deposito(deposito_nome)



    except ValueError:
        print('Coloque Uma Entrada Válida.')