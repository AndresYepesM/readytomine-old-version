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
from servicio.models import *
from .forms import *

# Create your views here.

#@login_required(login_url='/accounts/login')
# Mantenimiento home
#def ManteHome(request):

#	return render(request, 'mantenimiento/mante_home.html')

class ManteHomeList(ListView):
	# Listado de los pedidos de servicio
	model = Pedido
	template_name = 'mantenimiento/mante_home.html'


@login_required(login_url='/accounts/login/')
# Search Pedido resultado
def ManteBuscador(request):

	if request.method == 'POST':

			searched = request.POST['searched']
			servicio = Pedido.objects.filter(orden_pedido__contains=searched)
			return  render(request, 'mantenimiento/mante_buscador.html', {'searched':searched, 'servicio':servicio})
	else:
		return  render(request, 'mantenimiento/mante_buscador.html')

@login_required(login_url='/accounts/login/')
# Show clients information
def Workshop(request, pk):
	context = {'post': Pedido.objects.get(id=pk)}
	return render(request, 'mantenimiento/workshop.html', context)

class UpdateParte(UpdateView):
	model = Partes
	form_class = UpdateParteForm
	template_name = 'mantenimiento/parte_update.html'
	success_url = reverse_lazy('Mante_home')