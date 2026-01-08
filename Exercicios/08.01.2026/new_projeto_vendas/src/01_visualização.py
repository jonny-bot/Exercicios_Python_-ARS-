import pandas as pd

df = pd.read_csv('data/vendas.csv')

print(df.head())

df = df.drop_duplicates()

df['Preco_Unitario'] = df['Preco_Unitario'].astype(float)

df['Valor_Total'] = df['Quantidade'] * df['Preco_Unitario']

df['Valor_Total'] = df['Valor_Total'].map(lambda x: f"{x:.2f}")

print(df.head())