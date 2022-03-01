from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.usuariolist, name="usuario_list"),
    path('asistencia/', views.asistencia, name="asistencia"),
    path('nf/', views.usuariolist, name="notificaciones"),
    path('profile/', views.usuariolist, name="profile"),
    path('usuario_data/<int:id_usuario>/', views.usuario_data, name="usuario_data"),
    path('registro_cliente/', views.registro_cliente, name="registro_cliente"),
    path('search/', views.search, name='search'),
    path('form_cliente/', views.form_cliente, name='form_cliente'),
]