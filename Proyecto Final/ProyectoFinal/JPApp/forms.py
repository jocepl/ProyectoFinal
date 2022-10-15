from tkinter.ttk import Style
from django import forms

class investigaciones(forms.Form):

    nombre_dominio = forms.CharField(max_length=40)
    creador_investigacion = forms.CharField(max_length=40)
    nombre_investigacion = forms.CharField(max_length=40)
    fecha_investigacion = forms.DateField()
    resumen_investigacion = forms.CharField(max_length= 500)
    # investigation_media = 

class errores(forms.Form):

    dominio_error = forms.CharField(max_length= 20)
    fecha_error = forms.DateField()
    reportante_error = forms.CharField(max_length= 40)
    descripcion_error = forms.CharField(max_length= 500)
    #bugs_media = models.

class refuerzos(forms.Model):

    creador_tips = forms.CharField(max_length= 40)
    nombre_tips = forms.CharField(max_length= 250)
    descripcion_tips = forms.CharField(max_length= 500)
    fecha_tips = forms.DateField()
    email_tips = forms.EmailField()
    #media_tips = 
    link_tips = forms.URLField()