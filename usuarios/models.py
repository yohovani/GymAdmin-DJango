from django.db import models
from datetime import datetime

# Create your models here.

class Usuario(models.Model):

    genero_eleccion = (
        ('M', 'Masculino'),
        ('F', 'Femenino')
    )

    codigo = models.IntegerField()
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    nombre = models.CharField(max_length=100)
    profesion = models.CharField(max_length=100)
    genero = models.CharField(choices=genero_eleccion, max_length=100)
    ciudad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Asistencia(models.Model):
    fecha_asistencia = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.fecha_asistencia

class UsuarioAsistencia(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="usuario")
    asistencia = models.ForeignKey(Asistencia, on_delete=models.CASCADE, related_name="asistencia")
