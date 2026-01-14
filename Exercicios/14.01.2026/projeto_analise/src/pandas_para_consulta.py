# Instalação e Importação
import pandas as pd


# Lendo Tabelas
def dataFrames_series():
    dados = {
        'Nome': ['Joao', 'Natalia', 'Pedro'],
        'Idade': [24, 30, 24],
    }

    df = pd.DataFrame(dados)
    print(df)

    s = pd.Series([10, 20, 30])
    print(s)


def ler_arquivos_csv():
    # Ler Arquivos CSV
    df_csv = pd.read_csv('../data/vendas.csv')

    print(df_csv.head())


def ler_arquivos_json():
    # Ler Arquivos JSON
    df_json = pd.read_json('../data/vendas.json')

    print(df_json.head())


def ler_arquivos_excel():
    # Ler Arquivos Excel
    df_excel = pd.read_excel('../data/vendas.xlsx')

    print(df_excel.head())

    # Lendo apenas a aba "Sheet2"
    df_excel_sheet2 = pd.read_excel("../data/vendas.xlsx", sheet_name="Sheet2")

    print(df_excel_sheet2.head())  # mostra as primeiras linhas


def caminho_arquivos():
    '''

    Símbolos Importantes:

    . → representa a pasta atual

    .. → representa a pasta anterior (um nível acima)


    Exemplos práticos:

    projeto/
    │
    ├── script.py
    ├── data/
    │   └── vendas.json

    '''

    # Dentro do script.py:

    pd.read_json("data/vendas.json") # → acessa o arquivo dentro da pasta data.

    pd.read_json("./data/vendas.json") # → o mesmo que acima, ./ indica a pasta atual.

    pd.read_json("../data/vendas.json") # → sobe uma pasta e procura data/vendas.json (funciona se o script estiver dentro de uma subpasta).

    # Descobrir o diretório atual:

    import os
    print(os.getcwd())  # mostra a pasta atual


def manipuladno_basica_de_dados():
    df = pd.read_csv('../data/vendas.csv')

    # Mostrar as 1° Linhas da Tabela
    print(df.head())

    # Mostrar as Últimas Linhas das Tabelas
    print(df.tail())

    # Mostrar Apenas as Colunas 'Nome' e 'Idade'
    print(df[['pagamento', 'quantidade_vendida']])

    # Mostrar Apenas a Coluna 'Nome'
    print(df['quantidade_vendida'])


def serie_booleanas_e_filtros():
    df = pd.read_csv('../data/vendas.csv')

    print(df['quantidade_vendida'] > 4) # Retorna: TRUE

    # df[] - Filtra o DataFrame
    print(df[df['quantidade_vendida'] > 4])

    print(df[df['preco_unitario'] > 50])

    # Combinado Filtros
    filtro_maior_que_30 = df['quantidade_vendida'] > 4
    filtro_maior_que_5mil = df['preco_unitario'] > 50

    print(df[filtro_maior_que_30 & filtro_maior_que_5mil])

    # Operadores de Filtros

    # 1. AND( & ) - Seleciona linhas que satisfazem todas as condições.
    df_and = df[(df['quantidade_vendida'] > 4) & df['preco_unitario'] > 50]
    print(df_and)

    # 2. OR( | ) - Seleciona linhas que satisfazem pelo menos uma condição.
    df_or = df[(df['quantidade_vendida'] > 4) | (df['preco_unitario'] > 50)]
    print(df_or)

    # 3. NOT ( ~ ) - Inverte o filtro (seleciona quem não satisfaz a condição).
    df_not = df[~(df['quantidade_vendida'] > 4)]   # todos com idade <= 30
    print(df_not)

    # 4. Combinações múltiplas
    df_multipla = df[((df['quantidade_vendida'] > 4) & (df['preco_unitario'] > 50)) | (df['pagamento'] == "Cartão")]
    print(df_multipla)

    # Dicas importantes:
    # Sempre use parênteses em cada condição, senão o pandas pode dar erro de precedência.
    # Para filtros mais complexos, você pode criar variáveis intermediárias:
    filtro_idade = df['quantidade_vendida'] > 4
    filtro_salario = df['preco_unitario'] > 50
    filtro_cidade = df['pagamento'] == "Cartão"

    df_filtrados = df[filtro_idade & filtro_salario | filtro_cidade]
    print(df_filtrados)


def colunas_criando_removendo():
    df = pd.read_csv('../data/vendas.csv')

    # Criando Colunas
    coluna_criada = df['total_vendas'] = df['quantidade_vendida'] * df['preco_unitario']
    print(coluna_criada)

    # Removendo Colunas
    coluna_excluida = df.drop('total_vendas', axis=1)
    print(coluna_excluida)


def manipulando_colunas():
    df = pd.read_csv('../data/vendas.csv')

    # 1. Somando Valores de uma Coluna
    somar_coluna = df['preco_unitario'].sum()
    print(f'A Soma deu: {somar_coluna}')

    # 2. Média de uma Coluna
    media_coluna = df['preco_unitario'].mean()
    print(f'A Média Deu: {media_coluna:.2f}')

    # 3. Mínimo e Máximo
    minimo = df['preco_unitario'].min()
    maximo = df['preco_unitario'].max()
    print(f'Minimo: {minimo} \nMaximo: {maximo}')

    # 4. Desvio Padrão
    desvio_padrao = df['preco_unitario'].std()
    print(f'Desvio Padrão: {desvio_padrao:.2f}')

    # 5. Operações entre colunas
    # df['A+B'] = df['A'] + df['B']
    # df['A/B'] = df['A'] / df['B']

    # 6. Aplicar funções personalizadas
    # df['A'].apply(lambda x: x ** 2)  # quadrado dos valores da coluna A

    # 7. Resumo estatístico rápido
    estatistico_rapido = df.describe()
    print(estatistico_rapido)

    print(df.info())


def limpeza_dados():
    df = pd.read_csv('../data/vendas.csv')

    # Remove todas as linhas que possuem pelo menos um valor nulo
    print(df.dropna())

    # (Repetido) Remove todas as linhas que possuem pelo menos um valor nulo
    print(df.dropna())

    # Remove apenas as linhas onde a coluna 'Idade' possui valores nulos
    print(df.dropna(subset=['preco_unitario']))

    # Calcula a média da coluna 'quantidade_vendida' (ignorando os valores nulos)
    media_quantidade_vendida = df['preco_unitario'].mean()
    print(f'A Média de Idade é de: {media_quantidade_vendida}')

    # Substitui os valores nulos da coluna 'quantidade_vendida' pela média calculada
    df['preco_unitario'] = df['preco_unitario'].fillna(media_quantidade_vendida)
    print(df)  # Exibe o DataFrame com os valores nulos de 'quantidade_vendida' preenchidos

    # Converte a coluna 'quantidade_vendida' para o tipo inteiro (int)
    df['preco_unitario'] = df['preco_unitario'].astype(int)
    print(df)  # Exibe o DataFrame final, sem nulos e com 'Idade' como inteiro


def verificar_nan():
    df = pd.read_csv('../data/vendas.csv')

    print(df.isna())  # mostra onde estão os NaN

    print(df.isna().sum())  # conta quantos existem por coluna.

    print(df.isna().any())  # indica se há algum NaN por coluna.

    print(df.isna().values.any())  # verifica se existe algum NaN em todo o DataFrame.


def lidar_com_nan():
    df = pd.read_csv('../data/vendas.csv')

    # 1. Remover linhas ou colunas com NaN
    df.dropna()  # remove linhas com qualquer NaN

    df.dropna(axis=1)  # remove colunas com qualquer NaN

    # 2. Substituir valores NaN
    nan_por_zero = df.fillna(0)  # substitui NaN por 0
    print(nan_por_zero)

    valor_anterior = df.fillna(method="ffill")  # preenche com o valor anterior (forward fill)
    print(valor_anterior)

    valor_seguinte = df.fillna(method="bfill")  # preenche com o valor seguinte (backward fill)
    print(valor_seguinte)

    # 3. Substituir por estatísticas
    # df["A"].fillna(df["A"].mean(), inplace=True)  # média

    # df["B"].fillna(df["B"].median(), inplace=True)  # mediana

    # df["C"].fillna(df["C"].mode()[0], inplace=True)  # moda

    # 4. Identificar linhas com NaN
    linhas_com_nan = df[df.isna().any(axis=1)]
    print(linhas_com_nan)


def cortando_ocorrencias():
    df = pd.read_csv('../data/vendas.csv')

    print(df['pagamento'].value_counts())

    print(df['id_produto'].value_counts())


def operacao_de_agregacao():
    df = pd.read_csv('../data/vendas.csv')

    # Agrupa o DataFrame pela coluna 'id_produto'
    # Esse comando sozinho retorna um objeto GroupBy (não mostra os dados agregados ainda)
    print(df.groupby('id_produto'))

    # Calcula a média da coluna 'preco_unitario' para cada grupo de 'id_produto'
    print(df.groupby('id_produto')['preco_unitario'].mean())

    # Calcula a soma da coluna 'preco_unitario' para cada grupo de 'id_produto'
    print(df.groupby('id_produto')['preco_unitario'].sum())

    # Calcula o valor máximo da coluna 'preco_unitario' para cada grupo de 'id_produto'
    print(df.groupby('id_produto')['preco_unitario'].max())


def ordenando_dados():
    df = pd.read_csv('../data/vendas.csv')

    # Ordena o DataFrame pela coluna 'Salário' em ordem crescente (menor → maior)
    print(df.sort_values(by='preco_unitario'))

    # Ordena o DataFrame pela coluna 'Salário' em ordem decrescente (maior → menor)
    print(df.sort_values(by='preco_unitario', ascending=False))


def combinando_dados():
    df = pd.read_csv('../data/departamentos.csv')

    # Lê o arquivo 'departamentos.csv' que contém informações adicionais sobre os departamentos
    df_departamento = pd.read_csv('../data/departamentos.csv')
    print(df_departamento)  # Exibe o DataFrame de departamentos

    # Faz um merge (junção) entre df e df_departamento
    # Por padrão, o merge tenta usar colunas com o mesmo nome em ambos os DataFrames
    df_final = pd.merge(df, df_departamento)
    print(df_final)  # Exibe o resultado da junção

    # Faz o merge especificando explicitamente a coluna de junção
    # Aqui, a junção é feita pela coluna 'ID Departamento' presente em ambos os DataFrames
    df_final = pd.merge(df, df_departamento, left_on='ID Departamento', right_on='ID Departamento')
    print(df_final)  # Exibe o resultado da junção com chave definida

    # Lê o arquivo 'novos_funcionarios.csv' com dados de novos funcionários
    df_novo = pd.read_csv('../data/novos_funcionarios.csv')
    print(df_novo)  # Exibe os novos funcionários

    # Concatena (empilha) os DataFrames df e df_novo
    # ignore_index=True recria os índices de forma contínua no DataFrame final
    df_todos = pd.concat([df, df_novo], ignore_index=True)
    print(df_todos)  # Exibe todos os funcionários juntos (antigos + novos)

    #  Escrevendo Dados em Arquivos
    #  CSV
    df_todos.to_csv('../data/arquivos_salvos/todos_funcionarios_1.csv')

    # JSON
    df_todos.to_json('../data/arquivos_salvos/todos_funcionarios_1.json')

    #  EXCEL
    df_todos.to_excel('../data/arquivos_salvos/todos_funcionarios_1.xlsx')


while True:
    try:

        opcoes = {

            0:'sair do Programa',

            1:'dataFrames_series()',

            2:'ler_arquivos_csv()',

            3:'ler_arquivos_json()',

            4:'ler_arquivos_excel()',

            5:'manipuladno_basica_de_dados()',

            6:'serie_booleanas_e_filtros()',

            7:'colunas_criando_removendo()',

            8:'manipulando_colunas()',

            9:'limpeza_dados()',

            10:'verificar_naN()',

            11:'lidar_com_nan()',

            12:'cortando_ocorrencias()',

            13:'operacao_de_agregacao()',

            14:'ordenando_dados()',

            15:'combinando_dados()'

        }

        print("=== MENU DE OPÇÕES ===")
        for chave, valor in opcoes.items():
            print(f"{chave} - {valor}")

        escolha = int(input('Digite uma das Opções: '))

        match escolha:

            case 0:
                print('Fim do Programa!')
                break

            case 1:
                dataFrames_series()

            case 2:
                ler_arquivos_csv()

            case 3:
                ler_arquivos_json()

            case 4:
                ler_arquivos_excel()

            case 5:
                manipuladno_basica_de_dados()

            case 6:
                serie_booleanas_e_filtros()

            case 7:
                colunas_criando_removendo()

            case 8:
                manipulando_colunas()

            case 9:
                limpeza_dados()

            case 10:
                verificar_nan()

            case 11:
                lidar_com_nan()

            case 12:
                cortando_ocorrencias()

            case 13:
                operacao_de_agregacao()

            case 14:
                ordenando_dados()

            case 15:
                combinando_dados()

            case _:
                print(f'Você Digitou {escolha} Que não está entre 0 e 12')

    except ValueError:
        print(f'Digite uma Entrada Válida!')
