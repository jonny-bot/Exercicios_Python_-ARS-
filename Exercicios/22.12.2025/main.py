import pandas as pd


def mostrar_arquivo():
    df = pd.read_csv('alunos.csv')
    print(df)


def estatisticas_rapidas():
    df = pd.read_csv('alunos.csv')
    print(f"A Média das Notas é de: {df['nota'].mean():.2f}")
    print(f"A Idade Máxima é de: {df['idade'].max()}")


def media_notas():
    df = pd.read_csv('alunos.csv')
    print("Média de notas por curso")
    print(df.groupby('curso')['nota'].mean())


def cidade():
    df = pd.read_csv('alunos.csv')

    cidades = {
        1: 'São Paulo',
        2: 'Rio de Janeiro',
        3: 'Belo Horizonte',
        4: 'Curitiba',
        5: 'Porto Alegre',
        6: 'Recife',
        7: 'Fortaleza'
    }

    for codigo, nome in cidades.items():
        print(f"{codigo} - {nome}")

    numero_cidade = int(input("Digite o Número da Cidade: "))
    print(df[df['cidade'] == numero_cidade])


def alunos_matricularam():
    df = pd.read_csv('alunos.csv')
    ano = int(input("Digite um Ano: "))
    df['data_matricula'] = pd.to_datetime(df['data_matricula'])
    print(df[df['data_matricula'].dt.year == ano])


while True:

    try:

        opcoes = {
            0:'Sair do Programa',
            1:'Mostrar Dados',
            2:'Estatísticas rápidas',
            3:'Média de notas por curso',
            4:'Alunos por Cidade',
            5:'Quantos alunos se matricularam em XXXX'
        }

        for i, descricao in opcoes.items():
            print(f"{i} - {descricao}")

        opcao = int(input("Digite uma Opção: "))

        if opcao in opcoes:

            if opcao == 0:
                print("Saindo do Programa...")
                break

            elif opcao == 1:
                mostrar_arquivo()

            elif opcao == 2:
                estatisticas_rapidas()

            elif opcao == 3:
                media_notas()

            elif opcao == 4:
                cidade()

            elif opcao == 5:
                alunos_matricularam()

        else:
            print(f"Você Digitou {opcao}. Que não está entre 0 e {len(opcoes)-1}.")

    except ValueError:
        print("Digite uma Entrada Válida!")
