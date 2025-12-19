import pandas as pd

# Lendo o arquivo Excel
df = pd.read_excel("vendas_de_lanches.xlsx")

# Mostrando as primeiras linhas
print(f'{df.head()}')

# Informações básicas do DataFrame
print(f'{df.info()}')

# Estatísticas descritivas
print(f'{df.describe()}')
