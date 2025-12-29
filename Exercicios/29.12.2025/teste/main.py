import pandas as pd

nome_arquivo = 'arquivo_excel/arquivo_excel.xlsx'

df_aba1 = pd.read_excel(nome_arquivo)

filtro_1 = df_aba1[['Nota Python','Nota SQL','Nota Estatística']]
print(filtro_1)

df_aba2 = pd.read_excel(nome_arquivo, sheet_name='Plan2')

filtro_2 = df_aba2[df_aba2['Preço_Unitário'] > 100.00]
print(filtro_2)

#  Saber o nome das Colunas
colunas = df_aba1.columns
print(colunas)
print(df_aba2.columns)

