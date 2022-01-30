from links import links
from requests import get
from vivo_morto import vivo_morto


urls = links()
personagens = []

def requisicoes(url):
    personagem = get(url).json()
    return personagem['name'], personagem['status']

def execucao():
    for url in urls:
        x = requisicoes(url)
        personagens.append(x)


if __name__ == '__main__':
    
    execucao()

    for item in personagens:
        print(vivo_morto(item))