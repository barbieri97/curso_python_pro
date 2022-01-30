from links import links
from vivo_morto import vivo_morto
from requests import get
from json import loads
from multiprocessing import Pool

urls = links()

def requisicao(url):
    personagem = get(url).json()
    return personagem['name'], personagem['status']

def execucao():
    p = Pool(50)
    x = p.map(requisicao, urls)
    p.terminate()
    p.join()
    return x

if __name__ == '__main__':
    for item in execucao():
        print(vivo_morto(item))
