from requests import get
from bs4 import BeautifulSoup
from yaml import load, dump, FullLoader


url = 'https://www.w3schools.io/file/yaml-sample-example/'
resposta = get(url)
tags = BeautifulSoup(resposta.text, 'html5lib')

tag_yaml = tags.find('code', attrs={'class' : 'language-Yaml'})

comentarios = tag_yaml.find_all('span', attrs={'class' : 'c'})

lista_comentarios = [x.text for x in comentarios]

dict2yaml = {'comentarios' : lista_comentarios}

with open('comentarios_sem_regex.yml', 'w') as arq:
    dump(dict2yaml, arq)