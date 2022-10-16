import requests
from bs4 import BeautifulSoup

# parametros de url

#headers = {'User-Agent':, "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}

url = "https://empregos.maringa.com/?text=&estado=&cidade=&bairro=&tipo=&experiencia=N%C3%A3o&area=&faixa_salarial="

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
vagas = soup.find_all('div', class_='container')
profissao = soup.find_all('b', class_='mb-0 flex-wrap')
empresa = soup.find('div', class_='text-muted mt-1').get_text()
#city_day = soup.find('div', class_='d-none d-md-block')
cidade = soup.find('small', class_='text-nowrap').get_text()


for i in range(0, len (profissao)):
    print('Profissoes', soup.find_all('b', class_='mb-0 flex-wrap')[i].get_text())

#for i in range(0, len (empresa)):
#    print('Empresas', soup.find_all('div', class_='text-muted mt-1')[i].get_text())

#print(str('Empresa = '), empresa)
#print(str('Cidade = '), cidade)