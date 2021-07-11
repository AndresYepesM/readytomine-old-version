from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from mantenimiento import views
from .views import UpdateParte


urlpatterns = [

	#Home mantenimiento.
	path('servicios/', views.ManteHome, name='Mante_home'),

	#Mante resultado
	path('pedido/', views.ManteBuscador, name='Mante_pedido'),

	#Wrokshop del servicio
    re_path(r'Workshop_pedido/(?P<pk>\d+)$', views.Workshop, name='worshop'),

    #Update Parte
    re_path(r'^Actualizar_parte/(?P<pk>\d+)$', login_required(UpdateParte.as_view()), name='update_parte'),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)