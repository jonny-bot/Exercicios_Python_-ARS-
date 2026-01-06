import pandas as pd


def dataFrames_series():
    dados = {
        'Nome': ['Joao', 'Natalia', 'Pedro'],
        'Idade': [24, 30, 24],
    }

    df = pd.DataFrame(dados)
    print(df)

    s = pd.Series([10, 20, 30])
    print(s)


def lendo_tabelas():
    df = pd.read_csv('funcionarios.csv')
    print(df)


def manipuladno_basica_de_dados():
    df = pd.read_csv('funcionarios.csv')

    print(df.head())

    print(df.tail())

    print(df[['Nome', 'Idade']])

    print(df['Idade'])


def series_booleanas_e_filtros():
    df = pd.read_csv('funcionarios.csv')

    print(df['Idade'] > 30)

    print(df[df['Idade'] > 30])

    print(df[df['Salário'] > 5000])


def combinando_filtros():
    df = pd.read_csv('funcionarios.csv')

    filtro_maior_que_30 = df['Idade'] > 30
    filtro_maior_que_5mil = df['Salário'] > 5000

    print(df[filtro_maior_que_30 & filtro_maior_que_5mil])


def colunas_criando_removendo():
    df = pd.read_csv('funcionarios.csv')

    #  Criando Colunas
    df['Salário Anual'] = df['Salário'] * 12

    #  Removendo Colunas
    df = df.drop('Salário Anual', axis=1)
    print(df)


def resumindo_dados():
    df = pd.read_csv('funcionarios.csv')

    print(df.info())

    print(df.describe())

    print(df['Salário'].sum())

    print(df['Salário'].mean())


def limpeza_dados():
    df = pd.read_csv('funcionarios_nulos.csv')
    print(df)

    print(df.dropna())

    print(df.dropna())

    print(df.dropna(subset='Idade'))

    media_idade = df['Idade'].mean()
    df['Idade'] = df['Idade'].fillna(media_idade)
    print(df)

    df['Idade'] = df['Idade'].astype(int)
    print(df)


def cortando_ocorrencia():
    df = pd.read_csv('funcionarios.csv')

    print(df['Ativo'].value_counts())

    print(df['ID Departamento'].value_counts())


def operacao_de_agregacao():
    df = pd.read_csv('funcionarios.csv')

    print(df.groupby('ID Departamento'))

    print(df.groupby('ID Departamento')['Salário'].mean())

    print(df.groupby('ID Departamento')['Salário'].sum())

    print(df.groupby('ID Departamento')['Salário'].max())


def ordenando_dados():
    df = pd.read_csv('funcionarios.csv')

    print(df.sort_values(by='Salário'))

    print(df.sort_values(by='Salário', ascending=False))


def combinando_dados():
    df = pd.read_csv('funcionarios.csv')

    df_departamento = pd.read_csv('departamentos.csv')
    print(df_departamento)

    df_final = pd.merge(df, df_departamento)
    print(df_final)

    df_final = pd.merge(df,df_departamento, left_on='ID Departamento', right_on='ID Departamento')
    print(df_final)

    df_novo = pd.read_csv('novos_funcionarios.csv')
    print(df_novo)

    df_todos = pd.concat([df, df_novo], ignore_index=True)
    print(df_todos)

    #  Escrevendo Dados em Arquivos
    #  CSV
    df_todos.to_csv('todos_funcionarios_1.csv')

    #  ESCEL
    df_todos.to_excel('todos_funcionarios_1.xlsx')

while True:
    try:

        opcoes = {

            0:'sair do Programa',

            1:'dataFrames_series()',

            2:'lendo_tabelas()',

            3:'manipuladno_basica_de_dados()',

            4:'series_booleanas_e_filtros()',

            5:'combinando_filtros()',

            6:'colunas_criando_removendo()',

            7:'resumindo_dados()',

            8:'limpeza_dados()',

            9:'cortando_ocorrencia()',

            10:'operacao_de_agregacao()',

            11:'ordenando_dados()',

            12:'combinando_dados()'

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
                lendo_tabelas()

            case 3:
                manipuladno_basica_de_dados()

            case 4:
                series_booleanas_e_filtros()

            case 5:
                combinando_filtros()

            case 6:
                colunas_criando_removendo()

            case 7:
                resumindo_dados()

            case 8:
                limpeza_dados()

            case 9:
                cortando_ocorrencia()

            case 10:
                operacao_de_agregacao()

            case 11:
                ordenando_dados()

            case 12:
                combinando_dados()

            case _:
                print(f'Você Digitou {escolha} Que não está entre 0 e 12')

    except ValueError:
        print(f'Digite uma Entrada Válida!')
