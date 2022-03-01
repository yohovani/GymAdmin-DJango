from django.urls import path
from . import views

urlpatterns = [
    path('cierres_caja/',views.cierres, name="cierres_caja"),
]
