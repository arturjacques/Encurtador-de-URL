"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from pages.views import home_view
from encurtador.views import criar_link_view
from encurtador.views import teste_POST
import shorturl.path_functions

"""
Todos os URLs destinados para o sistema devem possuir um carácter especial
para que não seja criado um shortURL com o mesmo endereço de uma página do sistema.
"""

urlpatterns = [
    path('home.', home_view, name='home'),
    path('', home_view, name='home'),
    path('entrada.',criar_link_view, name='entrada'),
    path('teste.', teste_POST, name='teste'),
    path('admin./', admin.site.urls),
]

urlpatterns_secundario = shorturl.path_functions.urlpatterns

urlpatterns = urlpatterns+list(urlpatterns_secundario)