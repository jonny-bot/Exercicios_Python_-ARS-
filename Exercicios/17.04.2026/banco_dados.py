import mysql.connector

con = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="",
    database="meu_banco"
)

cursor = con.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    idade INT NOT NULL,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

dados = [
    ("Maria", 30),
    ("Carlos", 22),
    ("Ana", 27),
    ("Pedro", 35)
]

cursor.executemany(
    "INSERT INTO usuarios (nome, idade) VALUES (%s, %s)",
    dados
)

con.commit()


cursor.execute("SELECT * FROM usuarios")

for linha in cursor:
    print(linha)