from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="punto_venta"),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('search_product/', views.search_product, name='search_product'),
]