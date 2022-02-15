from django.urls import path
from . import views

urlpatterns = [
    path('registrar_pago/', views.registrar_pago, name='registrar_pago'),
]