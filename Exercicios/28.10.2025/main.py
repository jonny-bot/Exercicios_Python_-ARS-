import sqlite3


# Cria (ou conecta) ao banco de dados
conn = sqlite3.connect('meu_banco.db')
cursor = conn.cursor()


# Cria uma tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100),
    email VARCHAR(100),
    data_nascimento DATE
)
''')


#  Inserir Dados na Tabela
cursor.execute("INSERT INTO clientes (nome, email, data_nascimento) VALUES (?, ?, ?)", ("João", 'joao@gmail.com', '2025-03-31'))
cursor.execute("INSERT INTO clientes (nome, email, data_nascimento) VALUES (?, ?, ?)", ("Pedro", 'pedro@gmail.com', '2025-03-31'))


#  Deletar Usuario
#  cursor.execute("DELETE FROM clientes WHERE id = ?", (1,))


cursor.execute('SELECT * FROM clientes')
for row in cursor.fetchall():
    print(row)


# Salva e fecha (não mexer)
conn.commit() #  Salvar
conn.close() #  Fechar
