from django.urls import path
from JPApp import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.Home, name = "Inicio"),
    path("login/", views.Iniciar_sesion, name="Login"),
    path("registro/", views.Registro_usuarios, name="RegistroUsuario"),
    

    #CRUD 
    path("RegistroError/", views.RegistroErrores.as_view(), name = "BugsForm"),
    path("RegistroInvestigacion/", views.RegistroInvestigaciones.as_view(), name = "InvestigationForm"),
    path("RegistroRefuerzo/", views.RegistroRefuerzos.as_view(), name = "RefuerzosForm"),
    path("ListadoDeInvestigaciones/", views.ListaInvestigaciones.as_view(), name = "ListaInvestigacion"),
    path("ListadoDeErrores/", views.ListaErrores.as_view(), name = "ListaErrores"),
    path("ListadoDeRefuerzos/", views.ListaRefuerzos.as_view(), name = "ListaRefuerzos"),
    path("logout/", LogoutView.as_view(template_name="JPApp/logout.html"), name="Logout"),
]