from django.db import models

# Create your models here.

class Links (models.Model):
    link = models.CharField(max_length=400, name='link')
    data = models.DateField('data_pesquisa', auto_now_add=True )
    titulo = models.CharField('titulo da pagina', max_length=100)
    pontos = models.IntegerField('pontos', default=0)

    def __str__(self) -> str:
        return self.titulo
