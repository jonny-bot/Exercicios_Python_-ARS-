import pandas as pd

df = pd.read_csv('data/vendas.csv')

print(df.head())

df['Data'] = pd.to_datetime(df['Data'])
df = df.set_index("Data")

filtro_1 = df['Preço Unitário'] >= 50

filtro_2 = df['Quantidade'] > 2

filtro_3 = df.index <= '2026-01-11'

filtros_aplicados = df[filtro_1 & filtro_2 & filtro_3]

print(filtros_aplicados)
