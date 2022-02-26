from django.http import HttpResponse
from django.shortcuts import render
from crawler.raspagem import raspagem

# Create your views here.

def index(request):
    try:
        url = request.GET['url']
        x = raspagem.req(url)
        links1 = raspagem.niveis(x)
        links2 = raspagem.niveis(links1)

        
        contexto = {
            # 'titulo' : title,
            # 'link' : link,
            'links' : links2
        }
        return render(request, 'crawler/index.html', contexto)
    except:
        return render(request, 'crawler/index.html')