from django.contrib import admin
from .models import Usuario, Asistencia

# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('name','last_name','age','birth_date','genero','is_active')


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Asistencia)
