import pandas as pd
from openpyxl.utils.datetime import to_excel


def data_frame():
    df = pd.read_csv('data/vendas.csv')

    return df


dataFrame = data_frame()

dataFrame['total_vendido'] = dataFrame['quantidade_vendida'] * dataFrame['preco_unitario']

filtro = dataFrame[['nome_produto','quantidade_vendida','preco_unitario','total_vendido']]

filtro.to_excel('data/relatorio.xlsx')
