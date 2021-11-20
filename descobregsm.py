import requests
from bs4 import BeautifulSoup


fone = '84999053487'
url = "https://www.qualoperadora.net/"
payload = {'telefone':fone}
r = requests.post(url, payload)
#print(r.text)


soup = BeautifulSoup(r.text, 'html.parser')
#print(soup.prettify())
print(soup.find_all(class_='dados'))
print(soup.find_all(id='resultado'))






