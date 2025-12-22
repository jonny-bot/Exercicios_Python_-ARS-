import pandas as pd


# 1. Ler o arquivo CSV
def ler_arquivo_csv():
    df = pd.read_csv("alunos.csv")
    return df


df = ler_arquivo_csv()


# 2. Explorar os dados
print(df.head())        # primeiras linhas
print(df.info())        # informações gerais
print(df.describe())    # estatísticas descritivas

# 3. Seleção de colunas e linhas
print(df["nome"])       # coluna 'nome'
print(df.loc[0])        # primeira linha por rótulo
print(df.iloc[0])       # primeira linha por índice

# 4. Filtragem
print(df[df["curso"] == "Engenharia"])   # alunos de Engenharia
print(df[df["nota"] > 9])                # alunos com nota acima de 9

# 5. Operações estatísticas
print(df["nota"].mean())   # média das notas
print(df.groupby("curso")["nota"].mean())  # média por curso

# 6. Manipulação de colunas
df["aprovado"] = df["nota"] >= 7   # nova coluna booleana
print(df.head())

# 7. Ordenação
print(df.sort_values("nota", ascending=False))  # ordenar por nota

# 8. Tratamento de dados ausentes (se houvesse)
df = df.fillna("Desconhecido")

# 9. Trabalhando com datas
df["data_matricula"] = pd.to_datetime(df["data_matricula"])
print(df["data_matricula"].dt.year)   # extrair ano da matrícula

# 10. Exportar resultados
df.to_csv("alunos_processados.csv", index=False)
