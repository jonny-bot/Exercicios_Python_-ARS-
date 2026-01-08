import pandas as pd

# Carregar CSV
df = pd.read_csv("../data/vendas.csv")

# Ver primeiras linhas
print(df.head())

# Remover duplicatas
df = df.drop_duplicates()

# Converter colunas numéricas
df["Preço Unitário"] = df["Preço Unitário"].astype(float)
df["Quantidade"] = df["Quantidade"].astype(int)

# Criar coluna de valor total
df["Valor Total"] = df["Quantidade"] * df["Preço Unitário"]
