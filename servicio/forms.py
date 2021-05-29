from django import forms
from .models import *


class DateInput(forms.DateInput):
	input_type='date'

class NewPedido(forms.ModelForm):

	class Meta:
		model = Pedido
		widgets={'fecha_ingreso': DateInput(), 'fecha_egreso': DateInput()}
		fields = [
			'persona',
			'fecha_ingreso',
			'fecha_egreso',
			'suceso',
			'estado',
			'tracking',
		]
		labels = {
			'persona': 'Cliente',
			'fecha_ingreso': 'Fehca de ingreso',
			'fecha_egreso': 'Fecha de egreso',
			'suceso': 'suceso de la falla',
			'estado': 'estado del pedido',
			'tracking': 'Tracking number',
		}

class NewCliente(forms.ModelForm):
	class Meta:

		model = Cliente
		fields=[
			'nombre',
			'apellido',
			'cedula',
			'num_telf',
			'email',
			'direccion'
		]
		labels = {
			'nombre': 'Nombre del cliente',
			'apellido': 'Apellido del cliente',
			'cedula': 'Identificacion del cliente',
			'num_telf': 'Numero telefonico del cliente',
			'email': 'Correo del cliente',
			'direccion': 'Domicilio del cliente',
		}

class MostrarCliente(forms.ModelForm):
	class Meta:
		model = Cliente
		
		fields=[
			'nombre',
			'apellido',
			'cedula',
			'num_telf',
			'email',
			'direccion'
		]

		labels = {
			'nombre': 'Nombre del cliente',
			'apellido': 'Apellido del cliente',
			'cedula': 'Identificacion del cliente',
			'num_telf': 'Numero telefonico del cliente',
			'email': 'Correo del cliente',
			'direccion': 'Domicilio del cliente',
		}