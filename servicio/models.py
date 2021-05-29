from django.db import models

# Create your models here.

class Cliente(models.Model):
	nombre = models.CharField(max_length=65, verbose_name='Nombre del cliente')
	apellido = models.CharField(max_length=65, verbose_name='Apellido del cliente')
	cedula = models.IntegerField()
	num_telf = models.BigIntegerField()
	email = models.EmailField(max_length=254, verbose_name='Correo Electronico')
	direccion = models.CharField(max_length=500, verbose_name='Direccion del cliente')
	class Meta:
		ordering=["-id"]
		verbose_name_plural="Clientes"
	def __str__(self):
		return '{} {}'.format(self.nombre, self.apellido)

class Estado(models.Model):
	etapa = models.CharField(max_length=65, verbose_name='Etapa del proceso')
	class Meta:
		ordering=["-id"]
		verbose_name_plural="Etapa del pedido"
	def __str__(self):
		return str(self.etapa)

class Pedido(models.Model):
	persona = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
	fecha_ingreso = models.DateField()
	fecha_egreso = models.DateField(blank=True)
	suceso = models.TextField()
	estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True, blank=True)
	tracking = models.BigIntegerField()
	class Meta:
		ordering=["-id"]
		verbose_name_plural="Pedidos"

	def __str__(self):
		return '{} {}'.format(self.fecha_ingreso, self.persona)