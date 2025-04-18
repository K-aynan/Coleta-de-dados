### Arquivo coleta_dados em Python faz o seguinte:

### instale pacote Requests:
`pip install Requests`

Importa a biblioteca requests: usada para fazer requisições HTTP, ou seja, acessar páginas da web programaticamente.

Faz uma requisição GET para o site da InfoMoney na página do índice Ibovespa:

### Isso basicamente acessa a página como se você estivesse abrindo ela no navegador:
response = requests.get('https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/') 

### Imprime os primeiros 600 caracteres do conteúdo HTML retornado:
print(response.text[:600])

O conteúdo está em response.text, e [:600] mostra só o começo para não imprimir tudo.

Em resumo:
Esse script acessa a página do índice Ibovespa no site InfoMoney e mostra uma prévia do código-fonte HTML da página. 
Isso pode ser usado como parte de um web scraping para extrair dados financeiros, por exemplo.

### Arquivo conversor em Python faz o seguinte:

Importa `requests` e `BeautifulSoup`.

Desativa avisos de SSL.

Faz GET em `https://books.toscrape.com/`.

Converte o HTML em objeto `BeautifulSoup`.

Imprime os primeiros 2000 caracteres do HTML “bonitinho” (com `prettify()`).

