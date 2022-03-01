from django.http import JsonResponse
from django.shortcuts import render
from caja.models import CierreCaja
from datetime import date
import calendar

# Create your views here.
def cierres(request):
    today = date.today()
    dateMonthStart="%s-%s-01" % (today.year, today.month)
    cierre_cajas = CierreCaja.objects.filter(created_at__range=[dateMonthStart,today])
    total_cierres = 0
    for cierre in cierre_cajas:
        total_cierres+=cierre.total
    context = {
        'cierres':cierre_cajas,
        'total':cierre_cajas.count(),
        'total_cierres':total_cierres,
    }
    return render(request, 'caja/cierres.html', context)