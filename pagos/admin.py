from django.contrib import admin
from .models import Pago, TipoPago

# Register your models here.

admin.site.register(Pago)
admin.site.register(TipoPago)