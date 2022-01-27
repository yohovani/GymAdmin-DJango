from django.db import models
from usuarios.models import Usuario
from datetime import datetime

# Create your models here.

class TipoPago(models.Model):
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo

class Pago(models.Model):
    monto = models.FloatField(max_length=100)
    fecha_pago = models.DateTimeField(default=datetime.now())
    tipo = models.ForeignKey(TipoPago, on_delete=models.CASCADE)





