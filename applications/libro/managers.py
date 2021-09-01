from django.db import models
from django.db.models import Q

class LibroManager(models.Manager):
    def listar_libros(self,kword):
        resultado = self.filter(titulo__icontains = kword, fecha__range=('2000-01-01','2025-12-31'))
        return resultado

    def listar_libros2(self,kword,fecha1,fecha2):
        resultado = self.filter(titulo__icontains = kword, fecha__range=(fecha1,fecha2))
        return resultado