from django import forms
from .models import *

class DateInput(forms.DateInput):
	input_type='date'

class NewPedido(forms.ModelForm):

	class Meta:
		model = Pedido
		widgets={'fecha_ingreso': DateInput(), 'fecha_egreso': DateInput(), 'fehca_taller': DateInput()}
		fields = [
			'orden_pedido',
			'persona',
			'fecha_ingreso',
			'partes',
			'qr_code',
			'estado',
		]
		exclude = [
			'fecha_taller',
			'fecha_egreso',
		]
		labels = {
			'orden_pedido': 'orden del pedido',
			'persona': 'Seleccione el cliente de la orden',
			'fecha_ingreso': 'fecha de ingreso',
			'qr_code': 'Codigo qr se generara al terminar el registro.',
			'estado': 'estado del pedido',

		}


class UpdatePedido(forms.ModelForm):

	class Meta:
		model = Pedido
		widgets={'fecha_ingreso': DateInput(), 'fecha_egreso': DateInput(), 'fecha_taller': DateInput()}
		fields = [
			'persona',
			'fecha_ingreso',
			'fecha_taller',
			'fecha_egreso',
			'partes',
			'estado',
		]
		exclude =[
			'orden_pedido',

			'qr_code',
		]
		labels = {
			'orden_pedido': 'orden del pedido',
			'persona': 'Seleccione el cliente de la orden',
			'fecha_ingreso': 'fecha de ingreso',
			'fecha_taller': 'Fehca de ingreso al taller',
			'fecha_egreso': 'fecha de egreso',
			'qr_code': 'Codigo qr se generara al terminar el registro.',
			'estado': 'estado del pedido',

		}

class NewClient(forms.ModelForm):
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