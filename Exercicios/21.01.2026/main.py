import pandas as pd

df = pd.read_csv('data/vendas.csv')

print(df.head())

print(df.tail())

# Calcula o total de vendas corretamente
df['total_vendas'] = df['quantidade_vendida'] * df['preco_unitario']

print(df.head())

# Soma total das vendas
total_vendas = df['total_vendas'].sum()

print(f"Total das Vendas: R$ {total_vendas:.2f}")

# Média de Pagamentos
media_vendas = df['total_vendas'].mean()

print(f'Média Geral de Vendas: R$ {media_vendas:.2f}')

# Valores Min/Max
valor_min = df['total_vendas'].min() # Valor Minimo
valor_max = df['total_vendas'].max() # Valor Maximo

print(f'Valor Minimo: R$ {valor_min:.2f}')
print(f'Valor Máximo: R$ {valor_max:.2f}')

# Conta os tipos de pagamento
tipos_pagamentos = df['pagamento'].value_counts()

print(f'{tipos_pagamentos}')
