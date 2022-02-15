from django.db import models
from django.urls import reverse

# Create your models here.

class Usuario(models.Model):

    genero_eleccion = (
        ('M', 'Masculino'),
        ('F', 'Femenino')
    )

    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    age = models.IntegerField()
    birth_date = models.DateField(blank=False)
    genero = models.CharField(choices=genero_eleccion, max_length=100)
    is_active = models.BooleanField(default=True)
    direccion = models.CharField(max_length=500, blank=True)
    phone = models.CharField(max_length=15, blank=True)

    def get_url(self):
        return reverse('usuario_data', args=[self.pk])

    def __str__(self):
        return self.name


class Asistencia(models.Model):
    assist_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="usuario")

    def __str__(self):
        return str(self.assist_date)
