from distutils.command.build_scripts import first_line_re
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from JPApp.models import *
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

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
    
    return render(request, "JPApp/login.html", {"form1":form})

