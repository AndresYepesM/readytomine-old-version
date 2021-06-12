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
from .forms import NewPedido, UpdatePedido, NewClient, NewPart
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

class UpdatePedido(UpdateView):
	model = Pedido
	form_class = UpdatePedido
	template_name = 'servicios/update_pedido.html'
	success_url = reverse_lazy('listado_pedidos')

@login_required(login_url='/accounts/login')
def ShowOrder(request, pk):
	# Show Order information.
	context = {'posts': Pedido.objects.get(orden_pedido=pk)}
	return render(request,  'servicios/show_order.html', context)


@login_required(login_url='/accounts/login/')
# Show clients information
def ShowCliente(request, pk):
	context = {'posts': Cliente.objects.get(id=pk)}
	return render(request, 'servicios/show_cliente.html', context)


class NewClient(CreateView):
# new client class
	model = Cliente
	form_class = NewClient
	template_name = 'servicios/nuevo_cliente.html'
	success_url = reverse_lazy('Nuevo_cliente')

class NewPart(CreateView):

	model = Partes
	form_class = NewPart
	template_name='servicios/new_part.html'
	success_url=reverse_lazy('Nueva_parte')