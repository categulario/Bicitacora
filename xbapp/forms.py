# -*- coding:utf-8 -*-
from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

MODELO_USUARIO = get_user_model()

def valida_correo(correo):
    try:
        MODELO_USUARIO.objects.get(username=correo)
        raise ValidationError('ya existe este campo')
    except MODELO_USUARIO.DoesNotExist:
        pass

class APIRegistroForm(forms.Form):
    nombre              = forms.CharField(min_length=3, max_length=70)
    sexo                = forms.ChoiceField(choices=(
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ))
    fecha_nacimiento    = forms.DateField()
    correo              = forms.EmailField(validators=[valida_correo])
    password            = forms.CharField(min_length=6)