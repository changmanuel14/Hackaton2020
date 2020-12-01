"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('getPersonas/', getAllPersonas.as_view()),
    path('getPaises/', getAllPais.as_view()),
    path('getDepartamentos/', getAllDepartamento.as_view()),
    path('getMunicipio/', getAllMunicipio.as_view()),
    path('getGeneroNum/', getPersonaGenero.as_view()),
    path('getFemenino/', getFemenino.as_view()),
    path('getMasculino/', getMasculino.as_view()),
    path('getPersonasPais/', getPersonasPais.as_view()),
    path('getPersonasEdad/', getPersonasEdad.as_view()),
    path('getPersonaPais/', getPais.as_view()),
    path('getPersonaDepartamento/', getDepartamento.as_view()),
    path('getPersonaMunicipio/', getMunicipio.as_view()),
    path('newPersona/', NewPersona.as_view()),




]
