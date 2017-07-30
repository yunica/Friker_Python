from django import forms
from .models import Foto


class FormularioFoto(forms.ModelForm):
    class Meta:
        model = Foto
        fields = ('nombre', 'apellido')
