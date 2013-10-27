# -*- coding:utf-8 -*-
from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

MODELO_USUARIO = get_user_model()

def valida_ruta(ruta_dict):
    if 'hora_inicio' in ruta_dict and 'hora_fin' in ruta_dict and 'puntos' in ruta_dict:
        if type(ruta_dict['puntos'])==list:
            for punto in ruta_dict['puntos']:
                if 'latitud' in punto and 'longitud' in punto and 'altitud' in punto:
                    if type(punto['latitud']) != float or type(punto['longitud']) or type(punto['altitud']) != int or type(punto['indice']) != int:
                        raise ValidationError('formato de ruta invalido')
                else:
                    raise ValidationError('formato de ruta invalido')
    raise ValidationError('formato de ruta invalido')

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

class APILoginForm(forms.Form):
    correo              = forms.EmailField()
    password            = forms.CharField(min_length=6)