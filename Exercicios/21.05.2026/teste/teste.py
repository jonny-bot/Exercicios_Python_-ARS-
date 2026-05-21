import requests

# Endpoint da API
url = "https://api.hgbrasil.com/finance/stock_price"

# Parâmetros da requisição
params = {
    "symbol": "HGLG11",   # Ticker do FII
    "key": "SUA_CHAVE_API"  # Substitua pela sua chave da HG Brasil
}

# Fazendo a requisição
resposta = requests.get(url, params=params)

# Verificando se deu certo
if resposta.status_code == 200:
    dados = resposta.json()
    print("Dados do FII HGLG11:")
    print(dados)
else:
    print("Erro na requisição:", resposta.status_code)
