from django.urls import path, include
from .views import *


urlpatterns = [
    path('', empresa_listar, name='empresa_listar'),
    path('empresa/listar', empresa_listar, name='empresa_listar'),
    path('empresa/perfil/<int:id>', empresa_perfil, name='empresa_perfil'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register', include('django.contrib.auth.urls')),
]