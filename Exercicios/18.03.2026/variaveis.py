# ==========================================
# EXEMPLOS DE VARIÁVEIS EM PYTHON
# ==========================================

# 1. Atribuição básica (Tipos de Dados)
nome = "João"           # String (Texto)
idade = 25              # Integer (Número Inteiro)
altura = 1.75           # Float (Número Decimal)
estudando_python = True # Boolean (Verdadeiro ou Falso)

print("--- Dados do Aluno ---")
print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)
print("Estudando Python?", estudando_python)
print("\n")

# 2. Operações Matemáticas com Variáveis
ano_atual = 2026
ano_nascimento = ano_atual - idade

print("--- Operações Matemáticas ---")
print(nome, "nasceu aproximadamente em", ano_nascimento)

preco_curso = 150.00
desconto = 30.00
preco_final = preco_curso - desconto
print(f"O curso de Python com desconto custa: R$ {preco_final:.2f}")
print("\n")

# 3. Concatenando Strings (Juntando textos)
saudacao = "Olá"
mensagem = saudacao + " " + nome + ", seja bem-vindo ao Python!"

print("--- Textos (Strings) ---")
print(mensagem)
print("\n")

# 4. Tipagem Dinâmica (Mudando o tipo da variável)
idade = "Vinte e cinco" # A variável 'idade' que era Inteiro, agora virou String
print("--- Tipagem Dinâmica ---")
print("A idade agora está escrita como texto:", idade)
