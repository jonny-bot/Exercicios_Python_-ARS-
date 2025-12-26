# Instalar: pip install pandas openpyxl
import pandas as pd

# Caminho para o seu arquivo Excel
nome_arquivo = 'arquivo_excel/arquivo_excel.xlsx' # Ou 'caminho/para/seus_dados.xlsx'

# Ler o arquivo Excel (lê a primeira planilha por padrão)
df = pd.read_excel(nome_arquivo)

# Exibir as primeiras linhas do DataFrame
print(df.head())

# Para ler uma planilha específica (ex: 'Aba2')
df_aba2 = pd.read_excel(nome_arquivo, sheet_name='Plan2')

print(df_aba2.head())
