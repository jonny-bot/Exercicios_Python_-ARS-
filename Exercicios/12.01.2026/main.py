import pandas as pd


def total_vendas():
    df = pd.read_json('data/vendas.json')

    print(df.head())

    print(df.dtypes)

    df['quantidade_vendida'] = df['quantidade_vendida'].astype(float)

    # Arredondar preço unitário
    df['preco_unitario'] = df['preco_unitario'].round(2)

    # Calcular total vendido
    df['total_vendido'] = (df['quantidade_vendida'] * df['preco_unitario']).round(2)

    print(df.head())

    total_vendas = df['total_vendido'].sum()

    # Criar coluna formatada (string)
    df['total_vendido'] = df['total_vendido'].map(lambda x: f'R$ {x:.2f}')

    df['preco_unitario'] = df['preco_unitario'].map(lambda x: f'R$ {x:.2f}')

    print(df.head())

    print(f'Total de Vendas: R$ {total_vendas:.2f}')


def filtros():
    df = pd.read_json('data/vendas.json')

    print(df.head())

    # Cria as máscaras booleanas
    filtro_1 = df['pagamento'] == 'Pix'
    filtro_2 = df['preco_unitario'] > 300
    filtro_3 = df['vendedor'] > 'João'

    # Combina as máscaras
    filtros_aplicados = filtro_1 & filtro_2 & filtro_3

    # Aplica ao DataFrame
    df_filtrado = df[filtros_aplicados]

    print(df_filtrado)

filtros()
