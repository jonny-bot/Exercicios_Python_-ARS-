def ler_arquivos_json_pandas():
    import pandas as pd

    df = pd.read_json('data/vendas.json')

    print(df)


def ler_arquivos_json():
    import json

    with open("data/vendas.json", "r", encoding="utf-8") as arquivo:
        conteudo = json.load(arquivo)

        # df(DataFrame)
        for df in conteudo:
            print(f'Data Da Compra: {df['data_compra']} - ID do Produto: {df['id_produto']} - '
                  f'Nome Do Produto: {df['nome_produto']} - Cliente: {df['cliente']} - '
                  f'Forma de Pagamento: {df['pagamento']} - Vendedor: {df['vendedor']} - '
                  f'Quantidade Vendido: {df['quantidade_vendida']} - Preço Unitário: {df['preco_unitario']}')


ler_arquivos_json_pandas()
ler_arquivos_json()
