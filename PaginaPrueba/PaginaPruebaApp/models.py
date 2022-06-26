from tabnanny import verbose
from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=20)
    fecha_inicio = models.DateField()
    profesor = models.CharField(max_length=25)
    comision = models.IntegerField()

class Evento(models.Model):
    nombre_evento = models.CharField(max_length=30)
    fecha_inicio = models.DateField()
    disertante = models.CharField(max_length=30)

class Nosotros(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    estudios = models.CharField(max_length=30)
    acerca_de = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Nosotros"