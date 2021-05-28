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
from .forms import NewPedido
from .models import *

# Create your views here.

class ServicioList(ListView):
	# Listado de ususarios
	model = Pedido
	template_name = 'servicios/servicio_home.html'

class NewServicio(CreateView):
	# Editar de usuarios
	model = Pedido
	form_class = NewPedido
	template_name = 'servicios/nuevo_servicio.html'
	success_url = reverse_lazy('listado_pedidos')