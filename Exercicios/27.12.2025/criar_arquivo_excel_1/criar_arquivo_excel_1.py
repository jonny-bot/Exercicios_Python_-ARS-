import pandas as pd

# Exemplo de dados em dicionário
dados = {
    "Nome": ["Ana", "Carlos", "Maria"],
    "Idade": [25, 30, 28],
    "Cidade": ["São Paulo", "Rio", "Belo Horizonte"],
    "Salário": [3500, 4200, 3900]
}

# Criar DataFrame
df = pd.DataFrame.from_dict(dados)

# Exportar para Excel
df.to_excel("dados.xlsx", index=False)


