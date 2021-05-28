from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from servicio import views
from .views import ServicioList, NewServicio

urlpatterns = [

    # Pagina de inicio de Servicio y listado
    path('listado_servicios/', login_required(ServicioList.as_view()), name='listado_pedidos'),

    # New Servicio
    path('nuevo_pedido/', login_required(NewServicio.as_view()), name='Nuevo_pedido'),
    
]
