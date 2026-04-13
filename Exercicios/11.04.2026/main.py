import sqlite3


# Conectar ao banco (ou criar se não existir)
conexao = sqlite3.connect("nome_banco.db")
cursor = conexao.cursor()


# Criar tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS nome_tabela (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER
)
""")
conexao.commit()


# CREATE - Inserir usuário
def criar_usuario(nome, idade):
    # nome = input("Nome: ")
    # idade = int(input("Idade: "))

    cursor.execute("INSERT INTO nome_tabela (nome, idade) VALUES (?, ?)", (nome, idade))
    conexao.commit()
    print("Usuário criado com sucesso!")


# READ - Listar usuários
def listar_usuarios():
    cursor.execute("SELECT * FROM nome_tabela")
    # cursor.execute("SELECT idade FROM nome_tabela") -- para listar apenas a idade
    usuarios = cursor.fetchall()
    for u in usuarios:
        print(u)


# UPDATE - Atualizar usuário
def atualizar_usuario(id, nome, idade):
    # id = int(input("ID do usuário: "))
    # nome = input("Novo nome: ")
    # idade = int(input("Nova idade: "))

    cursor.execute(
        "UPDATE nome_tabela SET nome = ?, idade = ? WHERE id = ?",
        (nome, idade, id)
    )
    conexao.commit()
    print("Usuário atualizado com sucesso!")


# DELETE - Deletar usuário
def deletar_usuario(id):
    # id = int(input("ID do usuário: "))

    cursor.execute("DELETE FROM nome_tabela WHERE id = ?", (id,))
    conexao.commit()
    print("Usuário deletado com sucesso!")


# MENU simples
def menu():
    while True:
        print("\n1 - Criar usuário")
        print("2 - Listar usuários")
        print("3 - Atualizar usuário")
        print("4 - Deletar usuário")
        print("5 - Sair")

        opcao = input("Escolha: ")

        # Inserir Dados
        if opcao == "1":
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            criar_usuario(nome, idade)

        # Listar Dados
        elif opcao == "2":
            listar_usuarios()

        # Atualizar Dados
        elif opcao == "3":
            id = int(input("ID do usuário: "))
            nome = input("Novo nome: ")
            idade = int(input("Nova idade: "))
            atualizar_usuario(id, nome, idade)

        # Deletar Dados
        elif opcao == "4":
            id = int(input("ID do usuário: "))
            deletar_usuario(id)

        # Sair
        elif opcao == "5":
            break

        else:
            print("Opção inválida!")


# Executar
if __name__ == "__main__":
    menu()
    conexao.close()