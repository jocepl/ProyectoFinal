from distutils.command.build_scripts import first_line_re
from pyexpat import model
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from JPApp.models import *
from JPApp.forms import *
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.urls import is_valid_path, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def Home(request):
    return render(request, 'JPApp/inicio.html')


def Iniciar_sesion(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            clave = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=clave)
        
            if user:

                login(request, user)

                return render(request, "JPApp/inicio.html", {"mensaje" : f'"Hola {user}!"'})
            
            else:

                return render(request, "JPApp/inicio/.html", {"mensaje": f'Datos incorrectos. Intenta de nuevo.'})
    
    else:

        form = AuthenticationForm()
    
    return render(request, "JPApp/Autenticacion/login.html", {"form1":form})


def Registro_usuarios(request):

    if request.method == "POST":

        formu = RegistroUsusarioForm(request.POST)
        if formu.is_valid():

            NombreUsuario = formu.cleaned_data["username"]
            formu.save()
            return render(request, "JPApp/inicio.html", {"mensaje" : f'" Usuario {NombreUsuario} creado. "'})
    else:
        formu = RegistroUsusarioForm()

    return render(request, "JPApp/Autenticacion/registrouser.html", {"form2": formu})


def EditarPerfil(request):

    usuario = request.user

    if request.method == 'POST':
        formu3 = EditarUsuarioForm(request.POST)

        if formu3.is_valid():

            informacion = formu3.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()

            return render(request, 'JPApp/inicio.html')
    
    else:
            formu3= EditarUsuarioForm(initial = {'email':usuario.email})
    
    return render(request, 'JPApp/Autenticacion/editaruser.html', {'formu3':formu3, 'usuario':usuario})


#Vistas de registros de los modelos

class RegistroInvestigaciones(LoginRequiredMixin, CreateView): #Creación del registro de modelo "Investigations"

    model = investigations
    template_name = "JPApp/Investigaciones/Registroinvestigacion.html"
    success_url = "/JPApp/ListadoDeInvestigaciones"
    fields = ['domain_name', 'investigation_owner', 'investigation_name','investigation_date','investigation_overview','investigation_media', 'investigation_link']



class RegistroErrores(LoginRequiredMixin, CreateView): #Creación del registro de modelo "Bugs"

    model = bugs
    template_name = "JPApp/Errores/Registroerror.html"
    success_url = "/JPApp/ListadoDeErrores"
    fields = ['bugs_domain', 'bugs_date', 'bugs_owner', 'bugs_name', 'bugs_description', 'bugs_blocking', 'bugs_media', 'bugs_image']



class RegistroRefuerzos(LoginRequiredMixin, CreateView): #Creación del registro de modelo "Tips"

    model = tips
    template_name = "JPApp/Errores/Registrorefuerzo.html"
    success_url = "/JPApp/ListadoDeRefuerzos"
    fields = ['tips_owner', 'tips_name', 'tips_description', 'tips_date', 'tips_email', 'tips_media', 'tips_link']


#Listados de los datos en formularios de modelos

class ListaInvestigaciones(ListView): #Read de investigaciones
    model = investigations
    template_name = "JPApp/Investigaciones/Investigaciones.html"


class ListaErrores(ListView): #Read de errores
    model = bugs
    context_object_name = 'bugs'
    queryset = bugs.objects.all()
    template_name = "JPApp/Errores/Errores.html"


class ListaRefuerzos(ListView): #Read de refuerzos
    model = tips
    template_name = "JPApp/Refuerzos/Refuerzos.html"

#Edición de los datos en formularios de modelos

class EditarInvestigaciones(UpdateView): #Editar investigaciones
    model = investigations
    template_name = "JPApp/Investigaciones/Investigaciones.html"
    fields = ['domain_name', 'investigation_owner', 'investigation_name',
    'investigation_date','investigation_overview','investigation_media', 
    'investigation_link']


class EditarErrores(UpdateView): #Editar errores
    model = bugs
    template_name = "JPApp/Errores/Errores.html"
    fields = ['bugs_domain', 'bugs_date', 'bugs_owner', 'bugs_name', 'bugs_description', 'bugs_blocking', 'bugs_media', 'bugs_image']


class EditarRefuerzos(UpdateView): #Editar refuerzos
    model = tips
    template_name = "JPApp/Refuerzos/Refuerzos.html"
    fields = ['tips_owner', 'tips_name', 'tips_description', 'tips_date', 'tips_email', 'tips_media', 'tips_link']

#Eliminación de los datos en formularios de modelos

class EliminarInvestigaciones(DeleteView): #Editar investigaciones
    model = investigations
    template_name = "JPApp/Investigaciones/Investigaciones.html"


class EliminarErrores(DeleteView): #Editar errores
    model = bugs
    template_name = "JPApp/Errores/Errores.html"


class EliminarRefuerzos(DeleteView): #Editar refuerzos
    model = tips
    template_name = "JPApp/Refuerzos/Refuerzos.html"
