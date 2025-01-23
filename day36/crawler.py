from bs4 import BeautifulSoup
import requests

url = "https://pt.wikipedia.org/wiki/star_wars"

response = requests.get(url)

if response.status_code == 200:
    print("sucesso ao acessar a pagina")
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    title = soup.title.string
    #print(title)
    
    paragrafo_um = soup.find('p').text#um elemento  do tipo p
    
    #print(paragrafo_um)
    
    paragrafos = soup.find_all('p')#todos elementos do tipo p
    
    if len(paragrafos) > 1:
        print(paragrafos[1].text)
        
    else:
        print("Nao foi possivel encontrar o segundo paragrafo")
    links = soup.find_all('a', href=True)[:5]
    
    for link in links:
        print(link['href'])
    
   