import pandas as pd

df = pd.read_csv('../data/vendas.csv')

print(df.head())

print(df.dtypes)

# Converter a coluna de int64 para float64 e salvar no DataFrame
df['quantidade_vendida'] = df['quantidade_vendida'].astype(float)

print(df.dtypes)

# Criar coluna de total de vendas
df['total_vendas'] = df['quantidade_vendida'] * df['preco_unitario']

# Formatar com 2 casas decimais e salvar
df['total_vendas'] = df['total_vendas'].map(lambda x: f'{x:.2f}')

df['preco_unitario'] = df['preco_unitario'].map(lambda x: f'{x:.2f}')

print(df.head())

print(df.dtypes)
