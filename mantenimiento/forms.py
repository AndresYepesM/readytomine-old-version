from django import forms
from servicio.models import *

class UpdateParteForm(forms.ModelForm):

	class Meta:
		model=Partes
		fields={
			'emplo_name',
		}

		labels={
			'emplo_name': 'Quien esta realizando el trabajo?'
		}