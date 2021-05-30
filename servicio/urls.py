from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from servicio import views
from .views import ServicioList, NewServicio, NewClient, ShowCliente, UpdatePedido

urlpatterns = [

    # Pagina de inicio de Servicio y listado
    path('listado_servicios/', login_required(ServicioList.as_view()), name='listado_pedidos'),

    # New Servicio
    path('nuevo_pedido/', login_required(NewServicio.as_view()), name='Nuevo_pedido'),

    # New Cliente
    path('nuevo_cliente/', login_required(NewClient.as_view()), name='Nuevo_cliente'),


    # Show Cliente
    re_path(r'^cliente/(?P<pk>\d+)$', login_required(ShowCliente.as_view()), name='cliente'),

    # Update Pedido
     re_path(r'^pedido/(?P<pk>\d+)$', login_required(UpdatePedido.as_view()), name='update_pedido'),

    # tracing number page
    re_path(r'^track_del_pedido/(?P<pk>\d+)$', views.TrackingPage, name='track_pedido')
]
