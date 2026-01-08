import pandas as pd

# Carregar CSV
df = pd.read_csv("../data/vendas.csv")

# Criar coluna de valor total
df["Valor Total"] = df["Quantidade"] * df["Preço Unitário"]

# 1. Vendas por categoria
vendas_categoria = df.groupby("Categoria")["Valor Total"].sum().sort_values(ascending=False)
print("\nVendas por Categoria:\n", vendas_categoria)

# 2. Vendas por região
vendas_regiao = df.groupby("Região")["Valor Total"].sum().sort_values(ascending=False)
print("\nVendas por Região:\n", vendas_regiao)

# 3. Vendas por metodo de pagamento
pagamentos = df["Método de Pagamento"].value_counts()
print("\nMétodos de Pagamento:\n", pagamentos)
