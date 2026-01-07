import pandas as pd
'''
df = pd.read_csv('Arquivos/vendas.csv')

# Criando DataFrames filtrados
df_livros = df[df['Categoria'] == 'Livros']

df_eletronicos = df[df['Categoria'] == 'Eletrônicos']

df_vestuario = df[df['Categoria'] == 'Vestuário']

df_utilidades = df[df['Categoria'] == 'Utilidades']

# Salvando em um único arquivo Excel com várias abas
with pd.ExcelWriter('filtros_aplicados.xlsx', engine='xlsxwriter') as writer: 
    df_livros.to_excel(writer, sheet_name='Livros', index=False)
    df_eletronicos.to_excel(writer, sheet_name='Eletronicos', index=False)
    df_vestuario.to_excel(writer, sheet_name='Vestuario', index=False)
    df_utilidades.to_excel(writer, sheet_name='Utilidades', index=False)
'''

# Mais Simples

import pandas as pd

df = pd.read_csv('Arquivos/vendas.csv')

with pd.ExcelWriter('filtros_aplicados.xlsx', engine='xlsxwriter') as writer:
    for categoria, dados in df.groupby('Categoria'):
        dados.to_excel(writer, sheet_name=categoria[:31], index=False)  # Excel limita nomes a 31 caracteres
