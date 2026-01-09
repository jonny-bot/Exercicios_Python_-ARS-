import pandas as pd

# Lê o arquivo CSV (mesmo que esteja salvo como .json, o conteúdo é CSV)
df = pd.read_csv('../data/vendas.csv')

# Converte para JSON no formato de lista de objetos
df.to_json('../data/vendas.json', orient='records', indent=4, force_ascii=False)

print("Arquivo convertido para JSON com sucesso!")
