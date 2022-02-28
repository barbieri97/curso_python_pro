from bs4 import BeautifulSoup
from requests import get
from urllib.parse import urljoin
from multiprocessing import Pool
from concurrent import futures

class Crawler():

    def __init__(self, url: str, nivel_max: int=5):
        self.visitado = set()
        self.fila = [(0, url)]
        self.nivel_max = nivel_max

    def req (self, url: str) -> str:
        """ faz um get no link informado e retorna o conteudo """
        return get(url).content
    
    def get_links(self, content: str, url: str) -> list:
        """ recebe o conteudo html e retorna todos os links no html """
        parser = BeautifulSoup(content, 'html5lib')
    
        return [urljoin(url, a['href']) for a in parser.find_all('a', href=True)]
    
    def process_page(self, depth: int, url: str):
        """ printa os links acessados e o seu nivel (só para monitoramento) """
        print(f'{depth} - {url}')


    def run(self, item):
        """ Pega o primeiro item da fila, adiciona na conjunto de links visitados
        faz a requisição através da função req()
        printa na tela o link (só para monitoramento)
        se o nivel desse link for menor do que o nivel maximo ele
        pega todos os links dessa página e armazena na fila.
         """
        try:
            nivel, url = item
            self.visitado.add(url)
            conteudo = self.req(url)
            self.process_page(nivel, url)
            if nivel < self.nivel_max:
                for link in self.get_links(conteudo, url):
                    if link not in self.visitado:
                        self.fila.append((nivel + 1, link))
        except:
            pass
    
    def crawler(self):
        """ Executa a função run em processamento assincrono """
        while len(self.fila) != 0:
            self.run(self.fila.pop(0))
        
        return self.visitado
        

                    
if __name__ == '__main__':
    c = Crawler('https://etandel.xyz/blog/2018-07-30-crawling-in-python-part1.html', nivel_max=1)
    c.crawler()

