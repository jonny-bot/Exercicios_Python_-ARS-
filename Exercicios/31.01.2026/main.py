import sqlite3

conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS contas_bancarias(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    saldo FLOAT DEFAULT 0.0,
    cpf TEXT NOT NULL UNIQUE
)''')

# cursor.execute('''
#     INSERT INTO contas_bancarias 
#     (nome, saldo, cpf) VALUES
#     ('João Silva', 1000, '12345678900'),
#     ('Maria Oliveira', 2500, '98765432100'),
#     ('Carlos Souza', 500, '45678912345')
# ''')

cursor.execute('''SELECT * FROM contas_bancarias''')
for contas in cursor.fetchall():
    id, nome, saldo, cpf = contas
    print(f"ID: {id} | Nome: {nome} | Saldo: {saldo} | CPF: {cpf}")

conexao.commit()