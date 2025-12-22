import pandas as pd

# Criar um DataFrame com dados fictícios
df = pd.read_csv("nome,idade,cidade.csv")

#print(f'A Média das Idade é de: {df["Idade"].mean()}')   # Média das idades
#print(f'A Maior Idade é de: {df["Idade"].max()}')    # Idade máxima
#print(f'A Menor Idade é de: {df["Idade"].min()}')    # Idade mínima

cidade_sp = (df[df['Cidade'] == 'São Paulo'])

cidade_sp.to_csv("pessoas_SP.csv", index=False)
