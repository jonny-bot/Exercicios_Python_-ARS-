import pandas as pd
import matplotlib.pyplot as plt

# ==============================
# Exemplo de dados fictícios
# ==============================
df = pd.read_csv('vendas/vendas.csv')

# Conferir os nomes das colunas
for colunas in df.columns:
    print(colunas)

# Se a coluna for 'data' em minúsculo:
df['Data'] = pd.to_datetime(df['Data'])
df = df.set_index("Data")

# ==============================
# Relatórios com resample
# ==============================
relatorio_diario = df.resample("D").sum()
relatorio_semana = df.resample("W").sum()
relatorio_semana_segunda = df.resample("W-MON").sum()

relatorio_mensal = df.resample("ME").sum()
relatorio_mensal_inicio = df.resample("MS").sum()

relatorio_trimestral = df.resample("QE").sum()
relatorio_trimestral_inicio = df.resample("QS").sum()

relatorio_semestral = df.resample("2QE").sum()

relatorio_anual = df.resample("YE").sum()
relatorio_anual_inicio = df.resample("YS").sum()

# ==============================
# Impressão dos relatórios
# ==============================
print("=== Relatório Diário ===")
print(relatorio_diario, "\n")

print("=== Relatório Semanal (Domingo) ===")
print(relatorio_semana, "\n")

print("=== Relatório Semanal (Segunda) ===")
print(relatorio_semana_segunda, "\n")

print("=== Relatório Mensal (Fim do mês) ===")
print(relatorio_mensal, "\n")

print("=== Relatório Mensal (Início do mês) ===")
print(relatorio_mensal_inicio, "\n")

print("=== Relatório Trimestral (Fim do trimestre) ===")
print(relatorio_trimestral, "\n")

print("=== Relatório Trimestral (Início do trimestre) ===")
print(relatorio_trimestral_inicio, "\n")

print("=== Relatório Semestral ===")
print(relatorio_semestral, "\n")

print("=== Relatório Anual (Fim do ano) ===")
print(relatorio_anual, "\n")

print("=== Relatório Anual (Início do ano) ===")
print(relatorio_anual_inicio, "\n")

relatorio_mensal.plot(kind="bar", figsize=(10,5), title="Vendas Mensais")
plt.show()
