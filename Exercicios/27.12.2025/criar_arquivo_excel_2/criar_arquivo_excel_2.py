from openpyxl import Workbook

# Criar novo arquivo
wb = Workbook()
aba = wb.active
aba.title = "Base de Dados"

# Inserir cabeçalhos
aba["A1"] = "Nome"
aba["B1"] = "Idade"
aba["C1"] = "Cidade"
aba["D1"] = "Salário"

# Inserir dados
dados = [
    ("Ana", 25, "São Paulo", 3500),
    ("Carlos", 30, "Rio", 4200),
    ("Maria", 28, "Belo Horizonte", 3900)
]

for i, linha in enumerate(dados, start=2):
    aba[f"A{i}"] = linha[0]
    aba[f"B{i}"] = linha[1]
    aba[f"C{i}"] = linha[2]
    aba[f"D{i}"] = linha[3]

# Salvar arquivo
wb.save("dados2.xlsx")

