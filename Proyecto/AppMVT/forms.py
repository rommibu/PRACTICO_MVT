
from django import forms 


class FormularioFamilia(forms.Form):
    nombre=forms.CharField(max_length=60)
    apellido=forms.CharField(max_length=60)
    dni=forms.FloatField()
    extranjero=forms.BooleanField()
    enfermedadbase=forms.CharField(max_length=20)
    mail=forms.EmailField()