import numpy as np

# Exemplo de dados
dados = [3, 4, 7, 9]

# Média
media = np.mean(dados)

# Desvio padrão (populacional)
desvio_padrao = np.std(dados)

# Coeficiente de variação
cv = (desvio_padrao / media) * 100

print(f"Média: {media:.2f}")
print(f"Desvio padrão: {desvio_padrao:.2f}")
print(f"Coeficiente de variação: {cv:.2f}%")

