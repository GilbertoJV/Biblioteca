from django.db import models
from django.db.models import Q

class AutorManager(models.Manager):
    def buscar_autores(self,kword):
        resultado = self.filter(nombre__icontains = kword)
        return resultado

    def buscar_autores2(self,kword):
        resultado = self.filter(Q(nombre__icontains = kword) | Q(apellidos__icontains = kword))
        return resultado

    def buscar_autores3(self,kword):
        resultado = self.filter(nombre__icontains=kword).exclude(Q(edad__icontains = 25) | Q(edad__icontains = 28))
        return resultado

    def buscar_autores4(self,kword):
        resultado = self.filter(edad__gt=22, edad__lt=28).order_by('nombre')
        return resultado