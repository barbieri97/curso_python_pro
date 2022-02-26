from requests import get
from bs4 import BeautifulSoup
from concurrent import futures

def req(x):
    requisicao = get(x)
    pagina = BeautifulSoup(requisicao.text, 'html5lib')
    tags = pagina.find_all('a')
    links = []
    for l in tags:
        try:
            l = l['href']
            if l[:4] == 'http':
                links.append(l)
        except:
            pass
    return links

def niveis(urls):
    with futures.ProcessPoolExecutor() as executor:
        l = [e for e in executor.map(req, urls)]

        links = []
        for x in l:
            for i in x:
                links.append(i)
    return links
        