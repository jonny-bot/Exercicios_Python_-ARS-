import pandas as pd

df = pd.read_csv("vendas.csv")

filtro = df[df['Categoria'] == 'Eletrônicos']

print(filtro)
