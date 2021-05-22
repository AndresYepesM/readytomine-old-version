from django.db import models
from django.contrib.auth.models import User, AbstractUser

class Empleado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_administracion = models.BooleanField(default = False, verbose_name = 'Administracion')
    is_mantenimiento = models.BooleanField(default = False, verbose_name = 'Mantenimiento')

    class Meta:
    	verbose_name_plural = "Empleados"
    def __str__(self):
    	return str(self.user.first_name)