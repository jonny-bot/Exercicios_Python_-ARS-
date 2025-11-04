import sqlite3

def criar_banco():
    conexao = sqlite3.connect('conta_bancaria.db')
    cursor = conexao.cursor()


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS conta_bancaria(
            id INTEGER PRIMARY KEY AUTOINCREMENT,  
            nome TEXT NOT NULL UNIQUE,           
            senha TEXT NOT NULL,         
            saldo_inicial REAL NOT NULL                    
        )''')

    conexao.commit()
    conexao.close()


def criar_contas(nome, senha, saldo_inicial):
    conexao = sqlite3.connect('conta_bancaria.db')
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO conta_bancaria (nome, senha, saldo_inicial) "
                   "VALUES (?, ?, ?)",(nome, senha, saldo_inicial))

    print('Conta Criado com Sucesso!!!')

    conexao.commit()
    conexao.close()


def autenticar_usuario(nome_autenticado, senha_autenticado):
    conexao = sqlite3.connect('conta_bancaria.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM conta_bancaria WHERE nome = ? AND senha = ?", (nome_autenticado, senha_autenticado))
    resultado = cursor.fetchone()

    conexao.close()

    if resultado:
        print('Usuário Autenticado com Sucesso!')
        return True
    else:
        print('Usuário ou Senha Incorretos!')
        return False


def sacar(nome_saque):
    conexao = sqlite3.connect('conta_bancaria.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM conta_bancaria WHERE nome = ?", (nome_saque, ))
    resultado = cursor.fetchone()

    if resultado:
        saldo_atual = resultado[3]
        print(f"Seu saldo atual é: R$ {saldo_atual:.2f}")

        saque = float(input("Quanto você quer sacar: "))
        if saque <= saldo_atual:
            novo_saldo = saldo_atual - saque
            cursor.execute("UPDATE conta_bancaria SET saldo_inicial = ? WHERE nome = ?", (novo_saldo, nome_saque))
            conexao.commit()
            print(f"Saque de R$ {saque:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente para o saque.")
    else:
        print("Usuário não encontrado.")

    conexao.close()


def depositar(nome_depositar):
    conexao = sqlite3.connect('conta_bancaria.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM conta_bancaria WHERE nome = ?", (nome_depositar, ))
    resultado = cursor.fetchone()

    saldo_atual = resultado[3]
    print(f"Seu saldo atual é: R$ {saldo_atual:.2f}")

    depitar = float(input("Quanto você quer depositar: "))
    novo_saldo = saldo_atual + depitar
    cursor.execute("UPDATE conta_bancaria SET saldo_inicial = ? WHERE nome = ?", (novo_saldo, nome_depositar))
    conexao.commit()
    print(f"Saque de R$ {depitar:.2f} realizado com sucesso.")

    conexao.close()


def transferir_dinheiro(origem, destino, valor):
    conn = sqlite3.connect('conta_bancaria.db')
    cursor = conn.cursor()

    cursor.execute("SELECT saldo_inicial FROM conta_bancaria WHERE nome = ?", (origem,))
    origem_data = cursor.fetchone()

    cursor.execute("SELECT saldo_inicial FROM conta_bancaria WHERE nome = ?", (destino,))
    destino_data = cursor.fetchone()

    if origem_data and destino_data:
        saldo_origem = origem_data[0]
        saldo_destino = destino_data[0]

        if valor <= saldo_origem:
            novo_saldo_origem = saldo_origem - valor
            novo_saldo_destino = saldo_destino + valor

            cursor.execute("UPDATE conta_bancaria SET saldo_inicial = ? WHERE nome = ?", (novo_saldo_origem, origem))
            cursor.execute("UPDATE conta_bancaria SET saldo_inicial = ? WHERE nome = ?", (novo_saldo_destino, destino))

            conn.commit()
            print(f"Transferência de R$ {valor:.2f} realizada com sucesso.")
        else:
            print("Saldo insuficiente para realizar a transferência.")
    else:
        print("Conta de origem ou destino não encontrada.")

    conn.close()


def emitir_estrato(extrato_nome):
    conexao = sqlite3.connect('conta_bancaria.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM conta_bancaria WHERE nome = ?", (extrato_nome,))
    resultado = cursor.fetchone()

    if resultado:
        print(f"\nExtrato da Conta:\nID: {resultado[0]}\nNome: {resultado[1]}\nSaldo: R$ {resultado[3]:.2f}\n")
    else:
        print("Conta não encontrada.")

    conexao.commit()
    conexao.close()


def deletar_usuario(usuario_deletar, senha_deletar):
    conexao = sqlite3.connect('conta_bancaria.db')
    cursor = conexao.cursor()

    confirmacao = int(input('Você deseja apagar realmente sua conta? \n1 - Sim || 2 - Não\n'))

    if confirmacao == 1:
        cursor.execute("DELETE FROM conta_bancaria WHERE nome = ? AND senha = ?", (usuario_deletar, senha_deletar))
        conexao.commit()

        if cursor.rowcount > 0:
            print('Usuário Deletado com Sucesso')
            conexao.close()
            return True
        else:
            print('Usuário ou Senha Incorretos!')
            conexao.close()
            return False

    elif confirmacao == 2:
        print('Operação Cancelada.')
        conexao.close()


criar_banco()


while True:
    try:
        print('1 - Criar Uma Conta\n'
              '2 - Autenticar Usuário\n'
              '3 - Realizar Saques\n'
              '4 - Realizar Depósitos\n'
              '5 - Realizar Transferência\n'
              '6 - Emitir Extrato\n'
              '7 - Deletar Usuário\n'
              '8 - Fim do Programa\n')

        opcoes = int(input('Digite uma das Opções: '))

        if opcoes == 1:
            nome = input('Digite um Nome: ')
            senha = input('Digite uma Senha: ')
            saldo_inicial = float(input('Digite um Valor Inicial: '))

            criar_contas(nome, senha, saldo_inicial)

        if opcoes == 2:
            nome_autenticado = input('Digite um Nome: ')
            senha_autenticado = input('Digite uma Senha: ')

            autenticar_usuario(nome_autenticado, senha_autenticado)

        if opcoes == 3:
            nome_saque = input("Digite Seu Nome: ")
            sacar(nome_saque)

        if opcoes == 4:
            nome_depositar = input("Digite seu nome: ")
            depositar(nome_depositar)

        if opcoes == 5:
            origem = input('Digite um Nome: ')
            destino = input('Digite o Nome da Conta Destino: ')
            valor = float(input('Digite o Valor a ser Trânsferido: '))
            transferir_dinheiro(origem, destino, valor)

        if opcoes == 6:
            extrato_nome = input('Digite o Nome da Conta: ')
            emitir_estrato(extrato_nome)

        if opcoes == 7:
            usuario_deletar = input('Digite um Usuário a ser Deletado: ')
            senha_deletar = input('Digite a sua Senha: ')
            deletar_usuario(usuario_deletar, senha_deletar)

        elif opcoes == 8:
            print('Fim do Programa!!!')
            break

    except ValueError:
        print('Digite uma Entrada Valida!!!')