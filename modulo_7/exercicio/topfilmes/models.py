from django.db import models

# Create your models here.


class TopFilms(models.Model):
    titulo = models.CharField('titulo do filme', max_length=100)
    genero = models.CharField('genero do filme', max_length=100)
    lancamento = models.DateField('data de lançamento')

    def __str__(self):
        return self.titulo
