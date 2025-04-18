import requests
from bs4 import BeautifulSoup
	
url = ('https://python.org.br/web/')
requisicao = requests.get(url)
soup = BeautifulSoup(requisicao.content, 'html.parser')

##print(soup.text.strip())


for linha_texto in soup.find_all('h2'):
    titulo = linha_texto.text.strip()
    print('Titulo: ',titulo)

contar_titulos = 0
contar_paragrafos = 0

for linha_texto in soup.find_all('h2', 'p'):
    if linha_texto.name == 'h2':
        contar_titulos += 1
    elif linha_texto.name == 'p':
        contar_paragrafos += 1
        print(contar_titulos)
        print(contar_paragrafos)

for titulo in soup.find_all('h2'):
  print('\n Titulo: ', titulo.text.strip())
  for link in titulo.find_next_siblings('p'):
    for a in link.find_all('a', href=True):
      print('Texto Link: ', a.text.strip, '| URL:', a["href"])  