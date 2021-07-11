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
from django.contrib.auth.forms import UserChangeForm
from .forms import *
from .models import *

# Create your views here.

def Home(request):
	# Pagina de inicio
	return render(request, 'home.html')


@login_required(login_url='/accounts/login/')
# PAgina de administracion
def Admin_home(request):
	return render(request, 'home_user.html')

@login_required(login_url = '/accounts/login/')
# Mensaje de creacion de ususario
def new_userMsj(request):
	return render(request, 'registration/new_user_success.html')

@login_required(login_url = '/accounts/login/')
# Mensaje de creacion de ususario
def update_userMsj(request):
	return render(request, 'registration/msjupdate.html')


@login_required(login_url = '/accounts/login/')
# Mensaje de creacion de ususario
def delete_userMsj(request):
	return render(request, 'registration/msjdelete_user.html')

@login_required(login_url='/accounts/login/')
# Registro de ususario
def signup(request):
	if request.method == 'POST':
		form = RegistroForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('nuevo_ususario')
	else:
		form = RegistroForm()
	return render(request, 'registration/singup.html', {'form': form})

class UserListView(ListView):
	# Listado de ususarios
	model = User
	template_name = 'registration/user_list.html'


class UpdateUser(UpdateView):
	# Editar de usuarios
	model = User
	form_class = UpdateForm
	template_name = 'registration/update_user.html'
	success_url = reverse_lazy('ususario_editado')

class DeleteUser(DeleteView):
	# Borrar ususario

	model = User
	template_name = 'registration/delete_user.html'
	success_url = reverse_lazy('ususario_eliminado')