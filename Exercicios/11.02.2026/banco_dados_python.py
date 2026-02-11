import mysql.connector

# Conectar ao banco
conexao = mysql.connector.connect(
    host="localhost",       # Servidor na Máquina
    user="root",            # Nome da Conexao
    password="",            # Nesse caso, sem senha
    database="nome_banco"   # Nome do Banco Criado
)

cursor = conexao.cursor()

# Criar tabela
cursor.execute("CREATE TABLE IF NOT EXISTS clientes ("
               "id INT AUTO_INCREMENT PRIMARY KEY, "
               "nome VARCHAR(100), "
               "email VARCHAR(100))")

# Inserir dado
cursor.execute("INSERT INTO clientes (nome, email) VALUES (%s, %s)", ("João", "joao@email.com"))
cursor.execute("INSERT INTO clientes (nome, email) VALUES (%s, %s)", ("Natalia", "natalia@email.com"))
cursor.execute("INSERT INTO clientes (nome, email) VALUES (%s, %s)", ("Pedro", "pedro@email.com"))
cursor.execute("INSERT INTO clientes (nome, email) VALUES (%s, %s)", ("Marta", "marta@email.com"))
conexao.commit()

# Consultar dados
cursor.execute("SELECT * FROM clientes")
for linha in cursor.fetchall():
    print(linha)

# Fechar
cursor.close()
conexao.close()
