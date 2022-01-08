from requests import get
from bs4 import BeautifulSoup
from yaml import dump
from re import findall, search

url = 'https://www.w3schools.io/file/yaml-sample-example/'
resposta = get(url)
tags = BeautifulSoup(resposta.text, 'html5lib')

tag_yaml = tags.find('code', attrs={'class' : 'language-Yaml'})

arq_yaml = tag_yaml.text

padrao = r'#.{1,50000}'

lista_comentarios = findall(padrao, arq_yaml)
for c in lista_comentarios:
    print(c)

dict2yaml = {'comentarios' : lista_comentarios}

with open('comentarios_com_regex.yml', 'w') as arq:
    dump(dict2yaml, arq)