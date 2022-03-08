from django.db import models
from usuarios.models import Usuario
from datetime import datetime
from usuarios.models import Usuario
# Create your models here.

class TipoPago(models.Model):
    tipo = models.CharField(max_length=100)
    monto = models.FloatField(max_length=100)
    duracion = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.tipo

class Pago(models.Model):    
    fecha_pago = models.DateTimeField(default=datetime.now())
    tipo_pago = models.ForeignKey(TipoPago, on_delete=models.CASCADE, related_name='pago_tipo')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='pago_usuario')

    def __str__(self):
        return self.tipo_pago.tipo





