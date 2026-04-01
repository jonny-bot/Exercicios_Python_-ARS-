import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conexao = sqlite3.connect("meu_banco.db")
cursor = conexao.cursor()

# Criar tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    saldo REAL NOTE NULL DEFAULT 0.0,
    data_criacao TEXT DEFAULT
)
""")

# CREATE - Inserir dados
def inserir_usuario(nome, idade):
    cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", (nome, idade))
    conexao.commit()

# READ - Ler dados
def listar_usuarios():
    cursor.execute("SELECT * FROM usuarios")
    return cursor.fetchall()

# UPDATE - Atualizar dados
def atualizar_usuario(id, novo_nome, nova_idade):
    cursor.execute("UPDATE usuarios SET nome = ?, idade = ? WHERE id = ?", (novo_nome, nova_idade, id))
    conexao.commit()

# DELETE - Deletar dados
def deletar_usuario(id):
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    conexao.commit()

# Exemplo de uso
inserir_usuario("João", 25)
inserir_usuario("Pedro", 25)

print("Usuários cadastrados:")
print(listar_usuarios())

atualizar_usuario(1, "João Silva", 26)
print("Após atualização:")
print(listar_usuarios())

deletar_usuario(2)
print("Após exclusão:")
print(listar_usuarios())

# Fechar conexão
conexao.close()
