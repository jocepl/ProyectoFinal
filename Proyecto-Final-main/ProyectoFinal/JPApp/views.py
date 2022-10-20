from distutils.command.build_scripts import first_line_re
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from JPApp.models import *
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.urls import is_valid_path, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from JPApp.forms import FormularioEditarUser

# Create your views here.

#Página inicial

def Home(request):
    return render(request, 'JPApp/inicio.html')

#Views de autenticación

def Iniciar_sesion(request): #Vista para el inicio de sesión

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            clave = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=clave)
        
            if user:

                login(request, user)

                return render(request, "JPApp/inicio.html", {"mensaje" : f'"Hola {user}!"'}) #Muestra el mensaje de bienvenida para el usuario autenticado.
            
            else:

                return render(request, "JPApp/inicio/.html", {"mensaje": f'Datos incorrectos. Intenta de nuevo.'}) #Muestra mensaje de error si hay datos inválidos.
    
    else:

        form = AuthenticationForm()
    
    return render(request, "JPApp/Autenticacion/login.html", {"form1":form})


def Registro_usuarios(request): #Vista para el registro de usuario

    if request.method == "POST":

        formu = UserCreationForm(request.POST)

        if formu.is_valid():

            NombreUsuario = formu.cleaned_data["username"]

            formu.save()

            return render(request, "JPApp/inicio.html", {"mensaje" : f'" Usuario {NombreUsuario} creado. "'}) #Muestra el nombre del usuario creado.
    else:
        
        formu = UserCreationForm()

    return render(request, "JPApp/Autenticacion/registrousuario.html", {"form2": formu})


#Vista editar usuario

def Editar_Usuario(request):

    usuario_online = request.ser
    
    if request.method == "POST":
        
        formulario1 = FormularioEditarUser(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            usuario_online.email = info["email"]
            usuario_online.password1 = info["password1"]
            usuario_online.password2 = info["password2"]

            usuario_online.save()

            return render(request, "JPApp/inicio.html")
    
    else:

        formulario1 = FormularioEditarUser(initial={"email":usuario_online.email, "password1":usuario_online.password1, "password2":usuario_online.password2})

    contexto = {"form3":formulario1, "usuario":usuario_online}

    return render(request, "JPApp/Autenticacion/editarperfil.html", contexto)


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
