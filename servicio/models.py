from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
	nombre = models.CharField(max_length=65, verbose_name='Nombre del cliente')
	apellido = models.CharField(max_length=65, verbose_name='Apellido del cliente')
	cedula = models.IntegerField()
	num_telf = models.BigIntegerField()
	email = models.EmailField(max_length=254, verbose_name='Correo Electronico')
	direccion = models.TextField(max_length=500, verbose_name='Direccion del cliente')
	class Meta:
		ordering=["-id"]
		verbose_name_plural="Clientes"
	def __str__(self):
		return '{} {}'.format(self.nombre, self.apellido)

class Partes(models.Model):
	tipo_parte = models.CharField(max_length=65, verbose_name='Tipo de parte')
	serial_parte = models.CharField(max_length=20, verbose_name= 'Serial de las parte')
	if_garantia = models.BooleanField(null=True)
	observacion = models.CharField(max_length=250, verbose_name='Observacion de la parte')
	emplo_name = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	class Meta:
		ordering=["-id"]
		verbose_name_plural ="Partes por arreglar"
	def __str__(self):
		return '{} {}'.format(self.tipo_parte, self.serial_parte)


class Pedido(models.Model):
	orden_pedido = models.BigIntegerField()
	persona = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
	fecha_ingreso = models.DateField()
	fecha_taller = models.DateField(null=True, blank=True)
	fecha_egreso = models.DateField(null=True, blank=True)
	partes = models.ManyToManyField(Partes)
	#qr_code = models.ImageField(upload_to='qr_codes', blank=True)

	class Meta:
		ordering=["-id"]
		verbose_name_plural="Pedidos"

	#def __str__(self):
	#	return '{} {}'.format(self.fecha_ingreso, self.persona)

	#def save(self, *args, **kwargs):
	#	qrcode_img = qrcode.make(self.orden_pedido)
	#	canvas = Image.new('RGB', (300, 300), '#ffffff')
	#	draw = ImageDraw.Draw(canvas)
	#	canvas.paste(qrcode_img)
	#	fname = f'qr_code-{self.orden_pedido}'+'.png'
	#	buffer = BytesIO()
	#	canvas.save(buffer,'PNG')
	#	self.qr_code.save(fname, File(buffer), save=False)
	#	canvas.close()
	#	super().save(*args, **kwargs)
