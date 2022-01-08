from requests import get
from bs4 import BeautifulSoup
from time import sleep

class TesteSpider():
    def __init__(self, url) -> None:
        self.url = url
        self.requisicao = get(url)
        self.pagina = BeautifulSoup(self.requisicao.text, 'html5lib')
        self.tags = self.pagina.find_all('a')
        self.links = []
        for l in self.tags:
            try:
                self.links.append(l['href'])
            except:
                pass
        self.titulo = self.pagina.title.text

    def link_wiki(self):
        """ devolve os links internos do dominio wikipedia.org """
        links_wiki = [l for l in self.links if l.find('wikipedia.org') == 11 or l.find('/wiki/') == 0 or l.find('wikipedia.org') == 9]
        self.links_completos = [f'https://pt.wikipedia.org{l}' if l.find('/wiki/') == 0 else l for l in links_wiki ]
        return self.links_completos

if __name__ == '__main__':
    while True:
        url = input('insira o link da wikipedia que deseja realizar o scrape:')
        if 'wikipedia.org' in url:
            break
        else:
            print('ooops, parece que esse link não é valido para esse script\n')
    print('\033[1;32macessando o link iformado')
    sleep(2)
    x = TesteSpider(url)
    print(f'\033[1;97mPágina principal: {x.titulo}')
    links = x.link_wiki()
    print('\033[1;32magurade enquanto acessamos as páginas secundarias')
    paginas_secundarias = []
    for i in links:
        try:
            paginas_secundarias.append(TesteSpider(i).titulo)
        except:
            pass
    print('\033[1;32maqui estão os titulos das páginas secundarias!')
    sleep(1)
    for i in paginas_secundarias:
        print(f'\033[1;97mPágina secundária: {i}')
    
