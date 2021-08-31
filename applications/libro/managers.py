from django.db import models
from django.db.models import Q

class AutorManager(models.Manager):
    def listar_libros(self,kword):
        resultado = self.filter(nombre__icontains = kword)
        return resultado