import sqlite3


# Create (Criar):
conexao = sqlite3.connect('meu_banco.db')
cursor = conexao.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        codigo TEXT NOT NULL UNIQUE,
        descricao TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        preco REAL NOT NULL
    )''')


# Inserir Dados
cursor.execute(''' INSERT INTO produtos (codigo, descricao, quantidade, preco)
VALUES (?, ?, ?, ?) ''', ('1001', 'martelo', 60, 59.99))

# Read (Ler/Buscar)
cursor.execute(''' SELECT * FROM produtos ''')

resultado = cursor.fetchall()

for i in resultado:
    print(f"ID: {i[0]} || CODIGO: {i[1]} || DESCRICAO: {i[2]} || QUANTIDADE: {i[3]} || PRECO: {i[4]}")

# Update (Atualizar)
cursor.execute("UPDATE produtos SET descricao = ? WHERE codigo = ?", ('prego', '1002'))

# Delete (Deletar)
cursor.execute("DELETE FROM produtos WHERE id = ?", (1,))

conexao.commit()
conexao.close()
