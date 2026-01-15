import pandas as pd

df_funcionarios = pd.read_csv('data/funcionarios.csv')

print(df_funcionarios)

df_departamentos = pd.read_csv('data/departamentos.csv')

print(df_departamentos)

df_final = pd.merge(df_funcionarios, df_departamentos, left_on='ID Departamento', right_on='ID Departamento')

df_final.to_excel('novo_funcionario.xlsx')
