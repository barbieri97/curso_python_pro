from requests import get

def requisicoes(url):
    personagem = get(url).json()
    with open(f"imagens/{personagem['name']}.jpeg", 'wb') as arq:
        img = get(personagem['image'])
        arq.write(img.content)


    return personagem['name'], personagem['status']
