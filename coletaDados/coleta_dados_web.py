import requests
from bs4 import BeautifulSoup
	
url = ('https://python.org.br/web/')
requisicao = requests.get(url)
soup = BeautifulSoup(requisicao.content, 'html.parser')

print(soup.text.strip[])