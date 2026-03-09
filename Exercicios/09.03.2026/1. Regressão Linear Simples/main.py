# Importa a biblioteca NumPy para manipulação de arrays
import numpy as np

import pandas as pd

df = pd.read_csv('dados.csv')

# Importa a classe LinearRegression do scikit-learn
from sklearn.linear_model import LinearRegression

# Cria o array X com valores de 1 a 5 e o transforma em matriz coluna
# Esse será o conjunto de variáveis independentes (entrada)
X = np.array(df["horas_estudo"]).reshape((-1,1))  # Variável independente (X)

# Cria o array y com valores correspondentes (saída)
# Esse será o conjunto de variáveis dependentes (resposta)
y = np.array(df["nota"])  # Variável dependente (y)

# Instancia o modelo de regressão linear
model = LinearRegression()

# Treina (ajusta) o modelo com os dados de entrada (X) e saída (y)
model.fit(X, y)

# Cria um novo valor de entrada para prever
new_X = np.array([6]).reshape((-1,1))

# Usa o modelo treinado para prever o valor de saída correspondente
predicted_y = model.predict(new_X)

# Exibe o coeficiente da regressão (inclinação da reta)
print("Coeficiente de regressão: ", model.coef_)

# Exibe o intercepto (valor de y quando X = 0)
print("Intercepto: ", model.intercept_)

# Exibe a previsão para o novo valor de X
print("Previsão para X = ", new_X[0][0], " : ", predicted_y[0])
