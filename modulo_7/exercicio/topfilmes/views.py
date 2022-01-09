from django.shortcuts import render
from .models import TopFilms

# Create your views here.


def home(request):
    filmes = TopFilms.objects.all()
    return render(request=request, template_name='home.html', context={'filmes' : filmes})
    