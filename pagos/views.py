from datetime import datetime, timedelta
from django.shortcuts import render
from usuarios.models import Usuario
from .models import TipoPago, Pago

# Create your views here.

def registrar_pago(request):
    if request.method == 'POST':
        id_user = request.POST['id_cliente']
        tipo_pago = request.POST['tipo_pago']
        user = Usuario.objects.get(pk=id_user)
        payment_type = TipoPago.objects.filter(tipo=tipo_pago)
        payment = Pago.objects.create(
            usuario=user,
            tipo_pago=payment_type[0]
        )
        payment.save()
        user.vencimiento += timedelta(days=payment_type[0].duracion)
        user.save()
        print(user.vencimiento)
    context = {
        'pago':payment_type[0],
        'usuario':user,
        'pago_detail':payment,
    }
    return render(request, 'modales/ticket.html', context)

