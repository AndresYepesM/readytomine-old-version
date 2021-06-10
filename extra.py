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