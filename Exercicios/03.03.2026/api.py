# 1. Importar biblioteca de requisições
import requests

# 2. Definir a URL da API
url = "https://economia.awesomeapi.com.br/json/available"

# 3. Fazer a requisição
response = requests.get(url)

# 4. Verificar se deu certo
if response.status_code == 200:
    print("Requisição bem-sucedida!")
else:
    print("Erro na requisição:", response.status_code)

# 5. Tratar os dados recebidos
data = response.json()
print(data)

# 6. Usar Dados
for moeda in data:
    print(moeda)
