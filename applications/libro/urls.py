from django.urls import path
from . import views

urlpatterns = [
    path('libros/', views.ListLibros.as_view(), name='libros'),
    path('libros_2/', views.ListLibros2.as_view(), name='libros2'),
]
