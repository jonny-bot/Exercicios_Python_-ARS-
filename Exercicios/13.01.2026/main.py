import pandas as pd

# Lendo o arquivo JSON
df = pd.read_json('data/vendas.json')

print("Antes das transformações:")
print(df.head())

# Arredondando o preço unitário (mantendo como número)
df['preco_unitario'] = df['preco_unitario'].round(2)

# Calculando o total de vendas (mantendo como número)
df['total_vendas'] = df['quantidade_vendida'] * df['preco_unitario']

# Criando colunas formatadas para exibição
df['preco_unitario'] = df['preco_unitario'].map(lambda x: f'R$ {x:.2f}')

df['total_vendas'] = df['total_vendas'].map(lambda x: f'R$ {x:.2f}')

print("Depois das Alterações:")
print(df[['quantidade_vendida', 'preco_unitario', 'total_vendas']].head())


