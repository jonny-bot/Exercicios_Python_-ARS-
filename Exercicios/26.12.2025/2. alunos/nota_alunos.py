import pandas as pd

# Lendo o arquivo CSV (salve como alunos.csv)
df = pd.read_csv("nota_alunos.csv")

# 1. Calcular a média de cada aluno
df["Media"] = df[["Nota1","Nota2","Nota3"]].mean(axis=1)

# 2. Definir status (Aprovado se média >= 7, senão Recuperação)
df["Status"] = df["Media"].apply(lambda x: "Aprovado" if x >= 7 else "Recuperação")

print("Tabela com médias e status:\n", df[["Nome","Curso","Media","Status"]])

# 3. Quantos alunos aprovados e em recuperação
contagem_status = df["Status"].value_counts()
print("\nContagem de status:\n", contagem_status)

# 4. Maior média registrada
maior_media = df["Media"].max()
aluno_maior_media = df.loc[df["Media"].idxmax(), "Nome"]
print("\nMaior média:", maior_media, "-> Aluno:", aluno_maior_media)

# 5. Curso com mais aprovados
aprovados_por_curso = df[df["Status"]=="Aprovado"].groupby("Curso")["Nome"].count()
curso_top = aprovados_por_curso.idxmax()
print("\nCurso com mais aprovados:", curso_top)
