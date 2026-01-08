import pandas as pd

df = pd.read_csv('data/vendas.csv')

print(df.head())

# Criar coluna de Receita
df['Receita'] = df['Quantidade'] * df['Preco_Unitario']

# 1. Receita total
receita_total = df['Receita'].sum()

# 2. Produto mais vendido em quantidade
produto_mais_vendido = df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False).apply(lambda x: f"R$ {x:.2f}")

# 3. Produto que mais gerou receita
produto_maior_receita = df.groupby('Produto')['Receita'].sum().sort_values(ascending=False).apply(lambda x: f"R$ {x:.2f}")

# 4. Cliente mais recorrente
cliente_recorrente = df['Cliente'].value_counts()

# 5. Receita por vendedor
receita_vendedor = df.groupby('Vendedor')['Receita'].sum().sort_values(ascending=False).apply(lambda x: f"R$ {x:.2f}")

# 6. Formas de pagamento
pagamento = df['Pagamento'].value_counts()

# 7. Receita por dia
receita_dia = df.groupby('Data')['Receita'].sum()

# 8. Ticket médio
ticket_medio = df['Receita'].mean()

# Resultados
print(f"Receita Total: {receita_total}")
print(f"\nProduto mais vendido em quantidade: {produto_mais_vendido}")
print(f"\nProduto que mais gerou receita: {produto_maior_receita}")
print(f"\nCliente mais recorrente: {cliente_recorrente}")
print(f"\nReceita por vendedor: {receita_vendedor}")
print(f"\nFormas de pagamento: {pagamento}")
print(f"\nReceita por dia: {receita_dia}")
print(f"\nTicket médio: {ticket_medio}")
