import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados (pode ser de um CSV ou do DataFrame já salvo)
df = pd.read_csv("data/vendas.csv")   # supondo que você salvou os dados em vendas.csv

# Criar coluna de Receita
df['Receita'] = df['Quantidade'] * df['Preco_Unitario']

# Agrupamentos para gráficos
produto_mais_vendido = df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False)
produto_maior_receita = df.groupby('Produto')['Receita'].sum().sort_values(ascending=False)
receita_vendedor = df.groupby('Vendedor')['Receita'].sum().sort_values(ascending=False)
pagamento = df['Pagamento'].value_counts()
receita_dia = df.groupby('Data')['Receita'].sum()

# Gráfico 1: Top 5 produtos por quantidade
plt.figure(figsize=(10,6))
produto_mais_vendido.head(5).plot(kind='bar', color='skyblue')
plt.title("Top 5 Produtos por Quantidade")
plt.ylabel("Quantidade")
plt.xlabel("Produto")
plt.show()

# Gráfico 2: Top 5 produtos por receita
plt.figure(figsize=(10,6))
produto_maior_receita.head(5).plot(kind='bar', color='orange')
plt.title("Top 5 Produtos por Receita")
plt.ylabel("Receita (R$)")
plt.xlabel("Produto")
plt.show()

# Gráfico 3: Receita por vendedor
plt.figure(figsize=(10,6))
receita_vendedor.plot(kind='bar', color='green')
plt.title("Receita por Vendedor")
plt.ylabel("Receita (R$)")
plt.xlabel("Vendedor")
plt.show()

# Gráfico 4: Formas de pagamento
plt.figure(figsize=(8,6))
pagamento.plot(kind='bar', color='purple')
plt.title("Formas de Pagamento")
plt.ylabel("Quantidade de Vendas")
plt.xlabel("Forma de Pagamento")
plt.show()

# Gráfico 5: Receita por dia
plt.figure(figsize=(12,6))
receita_dia.plot(kind='line', marker='o', color='red')
plt.title("Receita por Dia")
plt.ylabel("Receita (R$)")
plt.xlabel("Data")
plt.xticks(rotation=45)
plt.show()
