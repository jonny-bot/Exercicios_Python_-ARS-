import json  # Importa o módulo JSON para manipular arquivos no formato JSON

# Função para carregar os dados dos usuários a partir de um arquivo JSON
def carregar_usuarios(caminho='Exercicios_JSON/exercicio1.json'):
    # Abre o arquivo no modo leitura com codificação UTF-8
    with open(caminho, 'r', encoding='utf-8') as arquivo:
        # Carrega e retorna os dados como uma lista de dicionários
        return json.load(arquivo)

# Função para calcular o IMC (Índice de Massa Corporal)
def calcular_imc(peso, altura):
    return peso / (altura ** 2)  # Fórmula do IMC: peso dividido pela altura ao quadrado

# Função para classificar o IMC de acordo com faixas padrão
def classificar_imc(imc):
    if imc <= 18.5:
        return 'abaixo do peso'
    elif imc <= 25:
        return 'peso normal'
    else:
        return 'sobrepeso'

# Função para exibir os dados básicos de cada usuário
def mostrar_usuarios(usuarios):
    for i in usuarios:
        # Exibe nome, idade, sexo (True para homem), peso e altura
        print(i['nome'], i['idade'], i['homem'], i['peso'], i['altura'])

# Função para mostrar o IMC e a classificação de cada usuário
# Pode filtrar por sexo usando o parâmetro 'filtro' (True para homens, False para mulheres)
def mostrar_imc(usuarios, filtro=None):
    for i in usuarios:
        # Se não houver filtro ou o sexo do usuário corresponder ao filtro
        if filtro is None or i['homem'] == filtro:
            imc = calcular_imc(i['peso'], i['altura'])  # Calcula o IMC
            status = classificar_imc(imc)  # Classifica o IMC
            print(f"{i['nome']} tem IMC {imc:.2f} e está {status}")

# Função para calcular e exibir a média de IMC por sexo
def media_imc(usuarios, filtro):
    # Lista de IMCs dos usuários filtrados por sexo
    imcs = [calcular_imc(i['peso'], i['altura']) for i in usuarios if i['homem'] == filtro]
    # Lista de nomes dos usuários filtrados
    nomes = [i['nome'] for i in usuarios if i['homem'] == filtro]

    # Exibe o IMC individual e a classificação de cada usuário
    for nome, imc in zip(nomes, imcs):
        print(f"{nome} tem IMC {imc:.2f} e está {classificar_imc(imc)}")

    # Se houver IMCs calculados, exibe a média
    if imcs:
        media = sum(imcs) / len(imcs)
        genero = 'Homens' if filtro else 'Mulheres'
        print(f"A média de IMC dos {genero} é: {media:.2f}")

# Função para identificar e exibir a pessoa mais alta e mais baixa
def pessoa_alta_baixa(usuarios):
    # Encontra o usuário com maior altura
    mais_alta = max(usuarios, key=lambda i: i['altura'])
    # Encontra o usuário com menor altura
    mais_baixa = min(usuarios, key=lambda i: i['altura'])

    # Exibe os resultados
    print(f"A pessoa mais baixa é {mais_baixa['nome']} com {mais_baixa['altura']} cm.")
    print(f"A pessoa mais alta é {mais_alta['nome']} com {mais_alta['altura']} cm.")

# ===== Execução do programa principal =====

usuarios = carregar_usuarios()  # Carrega os dados dos usuários

mostrar_usuarios(usuarios)  # Exibe os dados básicos
print('=======//=======')
mostrar_imc(usuarios)  # Exibe IMC de todos os usuários
print('=======//=======')
mostrar_imc(usuarios, filtro=True)  # Exibe IMC apenas dos homens
print('=======//=======')
mostrar_imc(usuarios, filtro=False)  # Exibe IMC apenas das mulheres
print('=======//=======')
media_imc(usuarios, filtro=True)  # Média de IMC dos homens
print('=======//=======')
media_imc(usuarios, filtro=False)  # Média de IMC das mulheres
print('=======//=======')
pessoa_alta_baixa(usuarios)  # Exibe a pessoa mais alta e mais baixa