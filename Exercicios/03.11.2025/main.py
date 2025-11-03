# Importa o módulo sqlite3, que permite trabalhar com bancos de dados SQLite em Python.
import sqlite3

# Estabelece uma conexão com o banco de dados chamado 'nome_banco.db'.
# Se o arquivo não existir, ele será criado automaticamente.
conexao = sqlite3.connect('nome_banco.db')

# Cria um objeto cursor, que será usado para executar comandos SQL.
cursor = conexao.cursor()

# Executa um comando SQL para criar uma tabela chamada 'nome_tabela', caso ela ainda não exista.
cursor.execute('''
    CREATE TABLE IF NOT EXISTS nome_tabela(
        id INTEGER PRIMARY KEY AUTOINCREMENT,  
        codigo TEXT NOT NULL UNIQUE,           
        descricao TEXT NOT NULL,               
        quantidade INTEGER NOT NULL,           
        preco REAL NOT NULL                    
    )''')

#  cursor.execute('''
#  CRIE A TABELA nome_tabela SE ELA NÃO EXISTIR(
    # Coluna 'id' como chave primária, gerada automaticamente
    # Coluna 'codigo' do tipo texto(str), obrigatória e única
    # Coluna 'descricao' do tipo texto(str), obrigatória
    # Coluna 'quantidade' do tipo inteiro(int), obrigatória
    # Coluna 'preco' do tipo real (decimal)(float), obrigatória
#  )''')


#  Inserir Dados na Tabela
#  cursor.execute("INSERT INTO nome_tabela (codigo, descricao, quantidade, preco) VALUES (?, ?, ?, ?)", ("1001", 'parafuso', 50, 59.99))


#  Apagar todos os registros
#  cursor.execute("DELETE FROM nome_tabela")


#  Resetar o contador de ID (funciona apenas se AUTOINCREMENT foi usado)
#  cursor.execute("DELETE FROM sqlite_sequence WHERE name='nome_tabela'")


#  Deletar Usuario pelo ID.
#  cursor.execute("DELETE FROM nome_tabela WHERE id = ?", (1,))


#  Deletar Usuario pelo Código.
#  cursor.execute("DELETE FROM nome_tabela WHERE codigo = ?", (1001,))


#  Deletar Usuario pelo quantidade.
#  cursor.execute("DELETE FROM nome_tabela WHERE quantidade = ?", (50,))


#  Deletar Usuario pelo preco.
#  cursor.execute("DELETE FROM nome_tabela WHERE preco = ?", (59.99,))


#  Exibir Informações da tabela
cursor.execute('SELECT * FROM nome_tabela')
for i in cursor.fetchall():
    print(i)


# Salva e fecha (não mexer)
conexao.commit() #  Salvar
conexao.close() #  Fechar
