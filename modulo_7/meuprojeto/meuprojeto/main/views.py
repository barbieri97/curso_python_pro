from django.shortcuts import render
from .models import ProjectDjango
from .forms import UserForm

# Create your views here.
def homepage(request):
    return render(
        request=request,
        template_name='home.html',
        context={'cursos' : ProjectDjango.objects.all}
    )

def formulario(request):
    submitbutton = request.POST.get('submit')

    conteudo = str
    observacao = str

    form = UserForm(request.POST or None)
    if form.is_valid():
        conteudo = form.cleaned_data.get('conteudo')
        observacao = form.cleaned_data.get('observacao')

    context= {'form' : form, 'conteudo' : conteudo, 'observacao' : observacao, 'submitbutton' : submitbutton}

    return render(
        request=request,
        template_name='observacao.html',
        context=context
    )