from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from servicio import views
from .views import ServicioList, NewServicio, UpdatePedido, NewClient, NewPart, NewOrderSucces, DeletePedido, DeleteOrderSucces


urlpatterns = [

    # Pagina de inicio de Servicio y listado
    path('listado_servicios/', login_required(ServicioList.as_view()), name='listado_pedidos'),

    # New Servicio
    path('nuevo_pedido/', login_required(NewServicio.as_view()), name='Nuevo_pedido'),

    # Mensaje de exito
    path('nuevo_pedido_registrado/', login_required(NewOrderSucces.as_view()), name='New_Order_succes'),

    # New Cliente
    path('nuevo_cliente/', login_required(NewClient.as_view()), name='Nuevo_cliente'),

    # New Client success
    path('nuevo_cliente_agregado/', views.NewClientDone, name='cliente_done'),

    # New Part
    path('Nueva_parte_pedido/', login_required(NewPart.as_view()), name='Nueva_parte'),

    # Show Cliente
    re_path(r'^cliente/(?P<pk>\d+)$', views.ShowCliente, name='cliente'),

    # Show Order
    re_path(r'Vizualizar_pedido/(?P<pk>\d+)$', views.ShowOrder, name='Orden_pedido'),

    # Update Pedido
    re_path(r'^Actualizar_pedido/(?P<pk>\d+)$', login_required(UpdatePedido.as_view()), name='update_pedido'),

    # Delete Pedudo
    re_path(r'^Borrar_pedido(?P<pk>\d+)$', login_required(DeletePedido.as_view()), name='borrar_pedido'),

    #delete pedido success
     path('pedido_eliminado/', login_required(DeleteOrderSucces.as_view()), name='delete_success'),

    # Search Pedido
    path('Buscar_pedido/', views.SearchPedido, name='Buscar_Pedido'),

    # Result Pedido
    path('Resultado/', views.ResultServicio, name='Resultado_Pedido'),

    # tracing number page
    re_path(r'^track_del_pedido/(?P<pk>\d+)$', views.TrackingPage, name='track_pedido'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
