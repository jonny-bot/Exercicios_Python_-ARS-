import pandas as pd

df = pd.read_csv('Arquivos/vendas.csv')

# Calcula o total como número
df['Total Venda'] = (df['Quantidade'] * df['Preço Unitário']).round(2)

# Cria coluna formatada para exibição
df['Total Venda Formatado'] = df['Total Venda'].map(lambda x: f'R$ {x:.2f}')

print(df[['Produto', 'Total Venda Formatado', 'Método de Pagamento']])

print(f'Valor total de todas as vendas: R$ {df["Total Venda"].sum():.2f}')
