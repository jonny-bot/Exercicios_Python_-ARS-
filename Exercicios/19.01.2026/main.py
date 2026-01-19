import pandas as pd

df = pd.read_csv('data/tudo.csv')

print(df.head())

print(df.tail())

for i in df.columns:
    print(i)
