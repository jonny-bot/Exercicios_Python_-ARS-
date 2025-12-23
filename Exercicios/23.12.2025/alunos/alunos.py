import pandas as pd

df = pd.read_csv("alunos.csv")

filtro = ((df['ID'] > 10) & (df['Idade'] > 20) &
          (df['Cidade'] == 'São Paulo')) & (df['Nota'] > 5)
print(df[filtro])
