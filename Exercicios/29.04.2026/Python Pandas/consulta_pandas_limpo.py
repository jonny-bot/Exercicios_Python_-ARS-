import pandas as pd
import os


# =========================
# CRIAÇÃO DE DADOS
# =========================
def criar_dataframe_series():
    df = pd.DataFrame({
        'Nome': ['Joao', 'Natalia', 'Pedro'],
        'Idade': [24, 30, 24]
    })
    print(df)

    s = pd.Series([10, 20, 30])
    print(s)


# =========================
# LEITURA DE ARQUIVOS
# =========================
def ler_csv():
    df = pd.read_csv('../data/vendas.csv')
    print(df.head())


def ler_json():
    df = pd.read_json('../data/vendas.json')
    print(df.head())


def ler_excel():
    df = pd.read_excel('../data/vendas.xlsx')
    print(df.head())

    df_sheet2 = pd.read_excel('../data/vendas.xlsx', sheet_name="Sheet2")
    print(df_sheet2.head())


# =========================
# MANIPULAÇÃO BÁSICA
# =========================
def visualizar_dados():
    df = pd.read_csv('../data/vendas.csv')

    print(df.head())
    print(df.tail())

    print(df[['pagamento', 'quantidade_vendida']])
    print(df['quantidade_vendida'])


# =========================
# FILTROS
# =========================
def filtros():
    df = pd.read_csv('../data/vendas.csv')

    filtro = df['quantidade_vendida'] > 4
    print(df[filtro])

    df_filtrado = df[
        (df['quantidade_vendida'] > 4) &
        (df['preco_unitario'] > 50)
    ]
    print(df_filtrado)


# =========================
# COLUNAS
# =========================
def colunas():
    df = pd.read_csv('../data/vendas.csv')

    df['total_vendas'] = df['quantidade_vendida'] * df['preco_unitario']
    print(df.head())

    df = df.drop(columns=['total_vendas'])
    print(df.head())


# =========================
# ESTATÍSTICA
# =========================
def estatisticas():
    df = pd.read_csv('../data/vendas.csv')

    print("Soma:", df['preco_unitario'].sum())
    print("Média:", df['preco_unitario'].mean())
    print("Min:", df['preco_unitario'].min())
    print("Max:", df['preco_unitario'].max())
    print("Desvio padrão:", df['preco_unitario'].std())

    print(df.describe())
    print(df.info())


# =========================
# LIMPEZA DE DADOS
# =========================
def limpeza():
    df = pd.read_csv('../data/vendas.csv')

    print(df.isna().sum())

    media = df['preco_unitario'].mean()
    df['preco_unitario'] = df['preco_unitario'].fillna(media)

    df['preco_unitario'] = df['preco_unitario'].astype(int)

    print(df.head())


# =========================
# NAN
# =========================
def lidar_nan():
    df = pd.read_csv('../data/vendas.csv')

    print(df.isna().sum())

    print(df.fillna(0))

    print(df.fillna(method="ffill"))
    print(df.fillna(method="bfill"))

    print(df[df.isna().any(axis=1)])


# =========================
# AGRUPAMENTO
# =========================
def agrupamento():
    df = pd.read_csv('../data/vendas.csv')

    print(df.groupby('id_produto')['preco_unitario'].mean())
    print(df.groupby('id_produto')['preco_unitario'].sum())
    print(df.groupby('id_produto')['preco_unitario'].max())


# =========================
# ORDENAÇÃO
# =========================
def ordenar():
    df = pd.read_csv('../data/vendas.csv')

    print(df.sort_values(by='preco_unitario'))
    print(df.sort_values(by='preco_unitario', ascending=False))


# =========================
# MERGE E CONCAT
# =========================
def combinar():
    df = pd.read_csv('../data/departamentos.csv')
    df_dep = pd.read_csv('../data/departamentos.csv')

    df_merge = pd.merge(df, df_dep)
    print(df_merge)

    df_novo = pd.read_csv('../data/novos_funcionarios.csv')
    df_concat = pd.concat([df, df_novo], ignore_index=True)

    print(df_concat)


# =========================
# MENU
# =========================
def menu():
    opcoes = {
        0: 'Sair',
        1: 'Criar DataFrame/Series',
        2: 'Ler CSV',
        3: 'Ler JSON',
        4: 'Ler Excel',
        5: 'Visualizar dados',
        6: 'Filtros',
        7: 'Colunas',
        8: 'Estatísticas',
        9: 'Limpeza',
        10: 'NaN',
        11: 'Agrupamento',
        12: 'Ordenação',
        13: 'Combinar dados'
    }

    while True:
        print("\n=== MENU ===")
        for k, v in opcoes.items():
            print(f"{k} - {v}")

        try:
            escolha = int(input("Escolha: "))

            if escolha == 0:
                break

            elif escolha == 1:
                criar_dataframe_series()
            elif escolha == 2:
                ler_csv()
            elif escolha == 3:
                ler_json()
            elif escolha == 4:
                ler_excel()
            elif escolha == 5:
                visualizar_dados()
            elif escolha == 6:
                filtros()
            elif escolha == 7:
                colunas()
            elif escolha == 8:
                estatisticas()
            elif escolha == 9:
                limpeza()
            elif escolha == 10:
                lidar_nan()
            elif escolha == 11:
                agrupamento()
            elif escolha == 12:
                ordenar()
            elif escolha == 13:
                combinar()

        except ValueError:
            print("Entrada inválida!")


if __name__ == "__main__":
    menu()
