from django.contrib import admin
from .models import Usuario, Asistencia, UsuarioAsistencia

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Asistencia)
admin.site.register(UsuarioAsistencia)