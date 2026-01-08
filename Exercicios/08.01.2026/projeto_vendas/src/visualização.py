import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar dados
df = pd.read_csv("../data/vendas.csv")

# Criar coluna de valor total
df["Valor Total"] = df["Quantidade"] * df["Preço Unitário"]

# Definir estilo padrão
sns.set_style("whitegrid")

# Vendas por categoria
categoria = df.groupby("Categoria")["Valor Total"].sum().sort_values()
plt.figure(figsize=(8,5))
sns.barplot(x=categoria.index, y=categoria.values, palette="viridis")
plt.title("Vendas por Categoria")
plt.xlabel("Categoria")
plt.ylabel("Valor Total (R$)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Vendas por região
regiao = df.groupby("Região")["Valor Total"].sum().sort_values()
plt.figure(figsize=(8,5))
sns.barplot(x=regiao.index, y=regiao.values, palette="magma")
plt.title("Vendas por Região")
plt.xlabel("Região")
plt.ylabel("Valor Total (R$)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Métodos de pagamento
plt.figure(figsize=(6,6))
df["Método de Pagamento"].value_counts().plot.pie(
    autopct="%1.1f%%",
    colors=sns.color_palette("pastel"),
    startangle=90
)
plt.title("Distribuição dos Métodos de Pagamento")
plt.ylabel("")  # remove o rótulo automático do eixo Y
plt.tight_layout()
plt.show()
