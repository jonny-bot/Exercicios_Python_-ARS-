# Importa a biblioteca NumPy, que possui funções matemáticas e estatísticas
import numpy as np

# Lista de dados numéricos que será usada para calcular os quartis
dados = [7, 8, 5, 6, 3, 4, 9, 10, 12]

# Calcula o primeiro quartil (Q1), que corresponde ao percentil de 25%
Q1 = np.percentile(dados, 25)

# Calcula o terceiro quartil (Q3), que corresponde ao percentil de 75%
Q3 = np.percentile(dados, 75)

# Calcula o intervalo interquartílico (IQR), que é a diferença entre Q3 e Q1
IQR = Q3 - Q1

# Exibe os resultados na tela
print("Q1:", Q1)   # Mostra o valor do primeiro quartil
print("Q3:", Q3)   # Mostra o valor do terceiro quartil
print("IQR:", IQR) # Mostra o intervalo interquartílico
