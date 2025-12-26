import pandas as pd

df = pd.read_csv('vendas.csv')

# 1. Média de preço unitário
media_preco = df["Preco_Unitario"].mean()
print("Média de preço unitário:", round(media_preco, 2))

# 2. Quantidade total por categoria
quantidade_por_categoria = df.groupby("Categoria")["Quantidade"].sum()
print("\nQuantidade total por categoria:\n", quantidade_por_categoria)

# 3. Cidade com maior quantidade vendida
cidade_top = df.groupby("Cidade")["Quantidade"].sum().idxmax()
print("\nCidade com maior quantidade vendida:", cidade_top)

# 4. Produto mais caro
produto_mais_caro = df.loc[df["Preco_Unitario"].idxmax(), "Produto"]
print("\nProduto mais caro:", produto_mais_caro)

# 5. Produto mais barato
produto_mais_barato = df.loc[df["Preco_Unitario"].idxmin(), "Produto"]
print("\nProduto mais barato:", produto_mais_barato)

# 6. Valor total de vendas
df["Valor_Total"] = df["Quantidade"] * df["Preco_Unitario"]
valor_total = df["Valor_Total"].sum()
print("\nValor total de vendas:", round(valor_total, 2))
