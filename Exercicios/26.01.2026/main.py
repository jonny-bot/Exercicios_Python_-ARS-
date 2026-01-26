import pandas as pd
from PIL.ImageMath import lambda_eval

df = pd.read_csv('data/vendas.csv')

print(df.head())

print(df.tail())

vendas_totais = df['quantidade_vendida'] * df['preco_unitario']

print(f'{vendas_totais.map(lambda x: f'R$ {x:.2f}')}')

total_vendas = vendas_totais.sum()

print(f'Total de Vendas: R$ {total_vendas:.2f}')
