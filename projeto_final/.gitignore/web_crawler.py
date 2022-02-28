from bs4 import BeautifulSoup
from requests import get
from urllib.parse import urljoin
from queue import Queue
from multiprocessing import Pool


def req (url: str) -> str:
    return get(url).content

def get_links(content: str, url: str) -> list:
    parser = BeautifulSoup(content, 'html5lib')

    return [urljoin(url, a['href']) for a in parser.find_all('a', href=True)]

def process_page(depth: int, url: str):
    print(f'{depth} - {url}')

def crawler(url: str, nivel_max: int=5):
    # urls já visitadas
    visitado = set()

    # fila de urls para vistar
    fila = []
    # add o link inicial
    fila.append((0, url))


    while len(fila) != 0:
        try:
            nivel, url = fila.pop(0)
            if url not in visitado:
                visitado.add(url)
    
                conteudo = req(url)
                process_page(nivel, url)
                
                if nivel < nivel_max:
                    for link in get_links(conteudo, url):
                        if link not in visitado:
                            fila.append((nivel + 1, link))
        except:
            pass
    return visitado
if __name__ == '__main__':
    print(crawler('https://etandel.xyz/blog/2018-07-30-crawling-in-python-part1.html', nivel_max=1))

