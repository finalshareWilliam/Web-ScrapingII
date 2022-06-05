from bs4 import BeautifulSoup   #importacao da biblioteca BeautifulSoup, especificamente bs4.
import requests, re   #importacao das bibliotecas, requests, openpyxl e re.

def getLinks(url):  #def obtendo o url base.
    response = requests.get(url)
    return response.text

url= "https://enttry.com.br/contato"    #url base
html_links = getLinks(url)
soup = BeautifulSoup(html_links, 'html.parser')
for link in soup.find_all('a', attrs={'href': re.compile("^https://")}):    #selecionando todos os links na url base.
    print(link.get('href'))