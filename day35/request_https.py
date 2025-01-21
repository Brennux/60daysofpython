import requests

url = "https://api.chucknorris.io/jokes/random"

response = requests.get(url)

if response.status_code == 200:
    print("Susesso")
    data = response.json()
    
    print("essa eh a piada do chuck norris: ")
    print(data['value'])
else:
    print("Erro na requisicao")
    