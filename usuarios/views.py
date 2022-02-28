from configparser import MAX_INTERPOLATION_DEPTH
from datetime import datetime
from dateutil.relativedelta import relativedelta
from multiprocessing import context
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Asistencia, Usuario
from pagos.models import Pago, TipoPago
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

@login_required(login_url='login')
def usuariolist(request):
    get_usuarios = Usuario.objects.all()
    get_tipos_pago = TipoPago.objects.all()

    paginator = Paginator(get_usuarios, 10)
    page = request.GET.get('page')
    page_users = paginator.get_page(page)


    data = {
        'get_usuarios': page_users,
        'get_tipos_pago': get_tipos_pago,
    }

    return render(request, 'usuariolist.html', data)

@login_required(login_url='login')
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

@login_required(login_url='login')
def registro_cliente(request):
    if request.method == 'POST' and request.FILES['img_perfil']:
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        date_birth = request.POST['date_birth']
        date_birth = datetime.strptime(date_birth, "%Y-%m-%d")
        edad = relativedelta(datetime.now(), date_birth)

        genero = request.POST['genero']
        direccion = request.POST['direccion']
        phone = request.POST['phone']
        cliente = Usuario.objects.create(
            name = nombre,
            last_name = apellido,
            age = edad.years,
            birth_date = date_birth,
            genero = genero,
            is_active = True,
            direccion = direccion,
            phone = phone
        )
        cliente.photo = request.FILES.get('img_perfil')
        fss = FileSystemStorage()
        file = fss.save(nombre, request.FILES['img_perfil'])
        cliente.save()
    return redirect('usuario_list')

@login_required(login_url='login')
def search(request):
    get_tipos_pago = TipoPago.objects.all()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            usuarios =Usuario.objects.filter(Q(name__icontains=keyword) |Q(last_name__icontains=keyword))
    context = {
        'get_usuarios':usuarios,
        'get_tipos_pago':get_tipos_pago,
    }
    return render(request, 'usuariolist.html', context)

def asistencia(request):
    status = 500
    user_name = ""
    print(request.POST['code_user'])
    if request.method == 'POST':
        try:
            user = Usuario.objects.get(pk=request.POST['code_user'])
            asistencia = Asistencia()
            asistencia.user = user
            asistencia.save()
            status = 200
            user_name = str(user.name) + " " + str(user.last_name)
        except:
            pass
            print("Algo salio mal")
    data = {
        'status':status,
        'usuario': user_name,
    }
    return JsonResponse(data)
