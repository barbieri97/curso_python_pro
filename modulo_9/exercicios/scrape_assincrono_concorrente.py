from links import links
from requests import get
from concurrent import futures
from vivo_morto import vivo_morto

urls = tuple(links())

def requisicoes(url):
    personagem = get(url).json()
    return personagem['name'], personagem['status']

def execucao():
    with futures.ProcessPoolExecutor() as executor:
        personagens = [e for e in executor.map(requisicoes, urls)]
        return personagens

if __name__ == '__main__':
    
    lista = execucao()
    for item in lista:
        print(vivo_morto(item))