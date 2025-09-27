# 1. Criando uma Função

def minha_fucao():
    pass

# 2. A Função depende de valores externos?

# SIM -> Use argumentos
def soma(a, b):
    return a + b

print(soma(3, 4)) # 7

# SIM -> Use argumentos
def mensagem():
    print('Sistemas Iniciado!')

mensagem()

# 3. Use Argumentos

def saudacao(nome):
    print(f'Olá, {nome}!')

saudacao('João')

# 4. Use argumentos com valor default

def saudacao1(nome='Visitante'):
    print(f'Olá, {nome}!')

saudacao1() # Olá, Visitante!
saudacao1('Natalia') # Olá, Natalia!

# 5. Use *args / **kwargs

# Exemplo com *args (quantidade variável de valores):
def soma_varios(*numeros):
    return sum(numeros)
print(soma_varios(1, 2, 3, 4)) # 10

# Exemplo com **kwargs (argumentos nomeados):

def mostrar_dados(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")
mostrar_dados(nome="Ana", idade=25, cidade="São Paulo")

# 6. Puxando função dentro da função:

def saudacao2():
    print("Olá!")

def mensagem2():
    print("Antes da saudação...")
    saudacao2()  # Chamando a função `saudacao` dentro da função `mensagem`
    print("Depois da saudação...")

mensagem2()