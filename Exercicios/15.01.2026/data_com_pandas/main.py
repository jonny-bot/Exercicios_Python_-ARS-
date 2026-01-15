import pandas as pd

# Criando um DataFrame de exemplo com datas e vendas
df = pd.DataFrame({
    "data": pd.date_range("2024-01-01", periods=365, freq="D"),
    "vendas": range(365)
})

# Converter para datetime (boa prática)
df["data"] = pd.to_datetime(df["data"])

# Definir a coluna de data como índice
df = df.set_index("data")

# Relatórios com resample:
relatorio_mensal = df.resample("M").sum()       # Mensal
relatorio_trimestral = df.resample("Q").sum()   # Trimestral
relatorio_semestral = df.resample("2Q").sum()   # Semestral
relatorio_anual = df.resample("Y").sum()        # Anual

# Salvar em um arquivo Excel com múltiplas abas
with pd.ExcelWriter("data/relatorios_temporais.xlsx") as writer:
    relatorio_mensal.to_excel(writer, sheet_name="Mensal")
    relatorio_trimestral.to_excel(writer, sheet_name="Trimestral")
    relatorio_semestral.to_excel(writer, sheet_name="Semestral")
    relatorio_anual.to_excel(writer, sheet_name="Anual")
