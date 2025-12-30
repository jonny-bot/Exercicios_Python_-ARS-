import pandas as pd

nome_arquivo = 'arquivo_excel/arquivo_excel.xlsx'

df_aba1 = pd.read_excel(nome_arquivo, sheet_name='Plan1')

# & -> AND (E) , | -> OR (OU) , .isin([...]) -> mais prático quando você tem várias opções.
filtro_1 = df_aba1['Departamento'].isin(['TI', 'RH'])

filtro_2 = df_aba1['Salário'] > 3000

filtro_3 = df_aba1['Data_Contratação'] > '2021-08-01'

mostrar_filtro = df_aba1[filtro_1 & filtro_2 & filtro_3]

mostrar_filtro.to_excel('filtro_funcionario.xlsx')
