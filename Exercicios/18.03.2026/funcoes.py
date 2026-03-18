# ==========================================
# ENTENDENDO FUNÇÕES EM PYTHON
# ==========================================

# 1. Uma função simples sem parâmetros
def dar_boas_vindas():
    print("🤖 Olá! Bem-vindo ao mundo das funções em Python!")

# Para a função funcionar, nós "chamamos" ela pelo nome:
dar_boas_vindas()
dar_boas_vindas() # O poder das funções: posso reaproveitar o código quantas vezes quiser!
print("-" * 30)

# 2. Função com parâmetros (recebendo ingredientes)
def fazer_sanduiche(recheio):
    print(f"🍞 Pegando dois pães...")
    print(f"🧀 Colocando {recheio} no meio...")
    print("🍔 Sanduíche pronto!\n")

fazer_sanduiche("Queijo e Presunto")
fazer_sanduiche("Frango com Catupiry")
print("-" * 30)

# 3. Função que RETORNA um valor (entrega o resultado de volta)
def calcular_dobro(numero):
    resultado = numero * 2
    return resultado

# Guardando o valor que a função nos devolveu:
meu_numero = calcular_dobro(5)
print(f"O dobro de 5 é: {meu_numero}")
print(f"O dobro de 50 é: {calcular_dobro(50)}")
