
import requests

response = requests.get('https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/')
print(response.text[:600])