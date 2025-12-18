import numpy as np
import pandas as pd

dados = [19, 20, 35, 41, 18, 39, 20, 36, 25,
         16, 15, 33, 20, 8, 18, 16, 39, 19,
         18, 20, 18, 25, 15, 39, 20, 37, 36,
         36, 36, 35, 23, 35, 33, 30, 16, 28]

n = len(dados)

# Número de classes (Sturges)
k = int(1 + 3.3 * np.log10(n))

# Amplitude
A = max(dados) - min(dados)

# Largura da classe
h = int(np.ceil(A / k))

# Criando intervalos
classes = range(min(dados), max(dados) + h, h)

# Frequências
freq_abs, bins = np.histogram(dados, bins=classes)
freq_rel = freq_abs / n * 100
freq_acum = np.cumsum(freq_abs)

# Montando tabela
tabela = pd.DataFrame({
    "Intervalo de Classe": [f"{bins[i]} ─ {bins[i+1]-1}" for i in range(len(bins)-1)],
    "Frequência Absoluta": freq_abs,
    "Frequência Relativa (%)": np.round(freq_rel, 2),
    "Frequência Acumulada": freq_acum
})

print("Tabela de Distribuição de Frequência:\n")
print(tabela)

