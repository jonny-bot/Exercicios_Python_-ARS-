import pandas as pd

df = pd.read_csv('vendas.csv')

df['Total_Vendido'] = df['Preço Unitário'] * df['Quantidade']

print(df)
