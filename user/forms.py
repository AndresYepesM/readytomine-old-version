from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class RegistroForm(UserCreationForm):

	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
			'is_staff',
			'is_active',
			'is_superuser',
		]
		labels = {
			'username': 'Usuario',
			'first_name': 'Nombre',
			'last_name': 'Apellido',
			'is_staff':'Administracion',
			'is_active': 'Acceso al sistema',
			'is_superuser': 'Acceso completo al sistema',
			'email': 'correo electronico',
		}

class UpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
			'is_staff',
			'is_active',
			'is_superuser',
		]
		labels = {
			'username': 'Usuario',
			'first_name': 'Nombre',
			'last_name': 'Apellido',
			'is_staff':'Administracion',
			'is_active': 'Acceso al sistema',
			'is_superuser': 'Acceso completo al sistema',
			'email': 'correo electronico',
		}