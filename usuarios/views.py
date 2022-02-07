from datetime import date, datetime
from multiprocessing import context
from django.shortcuts import render
from .models import Asistencia, Usuario
from pagos.models import Pago

# Create your views here.

def usuariolist(request):
    get_usuarios = Usuario.objects.all()

    data = {
        'get_usuarios': get_usuarios
    }

    return render(request, 'usuariolist.html', data)

def usuario_data(request, id_usuario):
    usuario = Usuario.objects.get(pk=id_usuario)
    asistencias = Asistencia.objects.filter(user__pk=id_usuario)
    pagos = Pago.objects.filter(usuario__pk=id_usuario)
    context = {
        'usuario': usuario,
        'asistencias': asistencias,
        'pagos': pagos,
        'asistencias_count': asistencias.count,
        'pagos_count': pagos.count,
    }
    return render(request, 'usuario_detail.html', context)
