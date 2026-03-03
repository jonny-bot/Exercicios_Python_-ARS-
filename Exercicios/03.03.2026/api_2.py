import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
response = requests.get(url)

if response.status_code == 200:
    print("Requisição bem-sucedida!")
else:
    print("Erro na requisição:", response.status_code)

data = response.json()
print(data)

for i in data:
    print(f'{i}')
