from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.template import loader
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views import generic
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import NewPedido, NewCliente, MostrarCliente
from .models import *

# Create your views here.

class ServicioList(ListView):
	# Listado de los pedidos de servicio
	model = Pedido
	template_name = 'servicios/servicio_home.html'

class NewServicio(CreateView):
	# Creacion de nuevos pedidos de servicio
	model = Pedido
	form_class = NewPedido
	template_name = 'servicios/nuevo_servicio.html'
	success_url = reverse_lazy('listado_pedidos')

class NewClient(CreateView):
	# Creacion de nuevos clientes
	model = Cliente
	form_class = NewCliente
	template_name = 'servicios/nuevo_cliente.html'
	success_url = reverse_lazy('listado_pedidos')

class ShowCliente(UpdateView):
	# Mostrar datos clientes
	model = Cliente
	form_class = MostrarCliente
	template_name = 'servicios/show_cliente.html'
	success_url = reverse_lazy('listado_pedidos')


class UpdatePedido(UpdateView):
	model = Pedido
	form_class = NewPedido
	template_name = 'servicios/update_pedido.html'
	success_url = reverse_lazy('listado_pedidos')

def TrackingPage(request, pk):

	context = {'posts': Pedido.objects.get(id=pk)}
	return render(request, 'servicios/track_pedido.html', context)