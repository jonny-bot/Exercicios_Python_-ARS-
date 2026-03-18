import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

print("--- Exemplo Prático de Regressão Linear ---")

# 1. Dados: Tamanho da casa em m2 e Preço em milhares de Reais
# X precisa ser uma matriz (2D), por isso colchetes duplos
tamanho_casas = np.array([[50], [70], [90], [110], [130]]) 
preco_casas = np.array([200, 280, 400, 450, 520])

print("\n1. Criando o modelo e treinando com os dados...")
modelo = LinearRegression()
modelo.fit(tamanho_casas, preco_casas)

# 2. Fazendo a previsão para uma casa de 100m2
tamanho_nova_casa = np.array([[100]])
preco_previsto = modelo.predict(tamanho_nova_casa)

print(f"\n2. Previsão:")
print(f"-> Para uma casa de 100m2, o preço sugerido é de: R$ {preco_previsto[0]:.2f} mil")

# 3. Informações da reta
print(f"\n3. Entendendo a Matemática da Reta (y = ax + b):")
print(f"-> Coeficiente (a): {modelo.coef_[0]:.2f} (O preço sobe {modelo.coef_[0]:.2f} mil reais a cada 1 m2)")
print(f"-> Intercepto (b): {modelo.intercept_:.2f} (O valor base teórico)")

print("\n4. Gerando Gráfico...")
print("-> O gráfico abrirá em uma nova janela. Feche a janela do gráfico para encerrar o programa.")

# 4. Gráfico
plt.scatter(tamanho_casas, preco_casas, color='blue', label='Dados Reais (Casas Conhecidas)')
plt.plot(tamanho_casas, modelo.predict(tamanho_casas), color='red', label='Linha de Regressão (Modelo)')
plt.scatter(tamanho_nova_casa, preco_previsto, color='green', marker='X', s=100, label='Previsão (Casa de 100m2)') # ponto da previsão

plt.xlabel("Tamanho (m2)")
plt.ylabel("Preço (Milhares de R$)")
plt.title("Regressão Linear: Preço de Casas por Tamanho")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

print("\nPrograma finalizado!")
