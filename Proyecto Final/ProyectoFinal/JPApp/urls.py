from django.urls import path
from JPApp.views import *

urlpatterns = [
    path('', Home, name = "Inicio"),
    path("login/", Iniciar_sesion, name="Login"),
]