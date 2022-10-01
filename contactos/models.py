from django.db import models

# Create your models here.

class Grupo(models.Model):
    grupo = models.CharField(max_length=40, unique=True)

    def __str__(self) ->str:
        return self.grupo

    class Meta:
        ordering = ['grupo']

class Contactos(models.Model):
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=100)
    contacto = models.CharField(max_length=15, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    morada = models.CharField(max_length=400, null=True, blank=True)
    foto = models.ImageField(upload_to='images/', null=True, blank=True)
    grupo = models.ForeignKey(Grupo, on_delete=models.PROTECT)
    notas = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.nome + ' ' + self.sobrenome

    class Meta:
        ordering = ['nome']
