from django.urls import path

from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('cursos', cursos, name='cursos'),
    path('eventos', eventos, name='eventos'),
    path('formulario', formulario, name='formulario'),
    path('formulario/cursos', crear_formulario_curso, name='fc'),
    path('formulario/eventos', crear_formulario_evento, name='fe'),
    path('busqueda_curso', busqueda_curso, name='busqueda_curso'),
    path('buscar/', buscar, name='buscar'),
    path('resultado_busqueda', buscar, name='resultado_busqueda'),

]