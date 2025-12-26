import pandas as pd

# Lendo o arquivo CSV (salve como funcionarios.csv)
df = pd.read_csv("funcionarios_salarios.csv")

# 1. Salário médio da empresa
salario_medio = df["Salario"].mean()
print("Salário médio da empresa:", round(salario_medio, 2))

# 2. Funcionário com maior salário
func_mais_caro = df.loc[df["Salario"].idxmax(), ["Nome","Cargo","Salario"]]
print("\nFuncionário com maior salário:\n", func_mais_caro)

# 3. Funcionário com menor salário
func_mais_barato = df.loc[df["Salario"].idxmin(), ["Nome","Cargo","Salario"]]
print("\nFuncionário com menor salário:\n", func_mais_barato)

# 4. Salário médio por departamento
media_por_departamento = df.groupby("Departamento")["Salario"].mean()
print("\nSalário médio por departamento:\n", media_por_departamento)

# 5. Departamento com maior salário médio
dep_top = media_por_departamento.idxmax()
print("\nDepartamento com maior salário médio:", dep_top)

# 6. Funcionário mais antigo (menor Data_Admissao)
df["Data_Admissao"] = pd.to_datetime(df["Data_Admissao"])
func_mais_antigo = df.loc[df["Data_Admissao"].idxmin(), ["Nome","Cargo","Data_Admissao"]]
print("\nFuncionário mais antigo:\n", func_mais_antigo)

# 7. Total gasto com salários
total_salarios = df["Salario"].sum()
print("\nTotal gasto com salários:", round(total_salarios, 2))
