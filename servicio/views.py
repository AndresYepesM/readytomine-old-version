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

class NewOrderSucces(ListView):

	model = Pedido
	template_name = 'servicios/order_success.html'

class DeleteOrderSucces(ListView):

	model = Pedido
	template_name = 'servicios/order_delete_success.html'


class NewServicio(CreateView):
	# Creacion de nuevos pedidos de servicio
	model = Pedido
	form_class = NewPedido
	template_name = 'servicios/nuevo_servicio.html'
	success_url = reverse_lazy('New_Order_succes')

class UpdatePedido(UpdateView):
	model = Pedido
	form_class = UpdatePedido
	template_name = 'servicios/update_pedido.html'
	success_url = reverse_lazy('New_Order_succes')

class DeletePedido(DeleteView):

	model = Pedido
	template_name = 'servicios/delete_pedido.html'
	success_url = reverse_lazy('delete_success')

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
	success_url = reverse_lazy('cliente_done')

class NewPart(CreateView):

	model = Partes
	form_class = NewPart
	template_name='servicios/new_part.html'
	success_url=reverse_lazy('Nueva_parte')


@login_required(login_url='/accounts/login/')
# Search Pedido
def SearchPedido(request):
	return  render(request, 'servicios/search_servicio.html')

@login_required(login_url='/accounts/login/')
# New client success
def NewClientDone(request):
	return render(request, 'servicios/new_client_done.html')

	
@login_required(login_url='/accounts/login/')
# Search Pedido resultado
def ResultServicio(request):

	if request.method == 'POST':

			searched = request.POST['searched']
			servicio = Pedido.objects.filter(orden_pedido__contains=searched)
			return  render(request, 'servicios/result_servicio.html', {'searched':searched, 'servicio':servicio})
	else:
		return  render(request, 'servicios/result_servicio.htmll')


def TrackingPage(request, pk):
	# Show Order information.
	context = {'posts': Pedido.objects.get(orden_pedido=pk)}
	return render(request,  'servicios/track_pedido.html', context)