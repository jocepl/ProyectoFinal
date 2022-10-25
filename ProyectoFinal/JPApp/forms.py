from dataclasses import field
from tkinter.ttk import Style
from django import forms
from .models import bugs, investigations, tips
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistroUsusarioForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label="Ingrese una contraseña")
    password2 = forms.CharField(label="Repita la contraseña")

    class Meta:

        model = User
        fields = ["username", "email", "password1", "password2"]


class EditarUsuarioForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label="Ingrese una contraseña")
    password2 = forms.CharField(label="Repita la contraseña")

    class Meta:

        model = User
        fields = ["email", "password1", "password2"]
        help_texts = {k:"" for k in fields}

class investigaciones(forms.Form):

    nombre_dominio = forms.CharField(max_length=40, widget=forms.TextInput(attrs={"placeholder":"Nombre del dominio"}), help_text='Nombre del dominio.')
    creador_investigacion = forms.CharField(max_length=40, help_text='Creador/es de la investigación.')
    nombre_investigacion = forms.CharField(max_length=40, help_text='Nombre de la investigación.')
    fecha_investigacion = forms.DateField(help_text='Fecha de la investigación.')
    resumen_investigacion = forms.CharField(max_length= 500, help_text='Breve descripción de la investigación.')
    investigation_media = forms.FileField(help_text='Ingresa el archivo de la investigación.')

    class Meta:
        model = investigations
        fields = ['domain_name', 'investigation_owner', 'investigation_name','investigation_date','investigation_overview','investigation_media', 'investigation_link']


class errores(forms.Form):

    dominio_error = forms.CharField(max_length= 20, widget=forms.TextInput(attrs={"placeholder":"Dominio afectado"}), help_text='Nombre o código del error.')
    fecha_error = forms.DateField(help_text='Fecha en la que ocurrió el error.')
    reportante_error = forms.CharField(max_length= 40, help_text='Nombre o TAG del colaborador.')
    titulo_error = forms.CharField(max_length=40)
    descripcion_error = forms.CharField(max_length= 500, help_text='Descripción del error.')
    bloqueante_error = forms.BooleanField()
    bugs_media = forms.FileField(help_text='Ingresa el video del error.')
    imagen_error = forms.ImageField(help_text='Ingresa la imágen del error')

    class Meta:
        model = bugs
        fields = ['bugs_domain', 'bugs_date', 'bugs_owner', 'bugs_name', 'bugs_description', 'bugs_blocking', 'bugs_media', 'bugs_image']


class refuerzos(forms.Form):

    creador_tips = forms.CharField(max_length= 80, help_text='Nombre creador/es del refuerzo.')
    nombre_tips = forms.CharField(max_length= 250, help_text='Tema del refuerzo.')
    descripcion_tips = forms.CharField(max_length= 500, help_text='Breve descripción del refuerzo.')
    fecha_tips = forms.DateField(help_text='Fecha del refuerzo.')
    email_tips = forms.EmailField(help_text='Correo electrónico del creador/es.')
    media_tips = forms.FileField(help_text='Presentación del refuerzo')
    link_tips = forms.URLField(help_text='Link a la presentación del refuerzo.')

    class Meta:
        model = tips
        fields = ['tips_owner', 'tips_name', 'tips_description', 'tips_date', 'tips_email', 'tips_media', 'tips_link']