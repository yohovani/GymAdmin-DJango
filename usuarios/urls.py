from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.usuariolist, name="usuario_list"),
    path('pb/', views.usuariolist, name="punto_venta"),
    path('nf/', views.usuariolist, name="notificaciones"),
    path('profile/', views.usuariolist, name="profile")
]