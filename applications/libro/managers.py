from django.db import models
from django.db.models import Q, Count

class LibroManager(models.Manager):
    def listar_libros(self,kword):
        resultado = self.filter(titulo__icontains = kword, fecha__range=('2000-01-01','2025-12-31'))
        return resultado

    def listar_libros2(self,kword,fecha1,fecha2):
        resultado = self.filter(titulo__icontains = kword, fecha__range=(fecha1,fecha2))
        return resultado

    def listar_libros_categoria(self, categoria):
        return self.filter(categoria__id=categoria).order_by('titulo')

    def libro_num_prestamos(self):
        resultado = self.aggregate(num_prestamos=Count('libro_prestamo'))

        return resultado


class CategoriaManager(models.Manager):
    def categoria_por_autor(self, autor):
        return self.filter(categoria_libro__autores__id=autor)