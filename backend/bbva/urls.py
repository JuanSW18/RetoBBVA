"""bbva URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from bbva.backend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login', views.login),
    path('cuentas_bancarias/<int:id_usuario>', views.get_list_cuentas_bancarias),
    path('recibos', views.listar_recibos),
    path('servicios', views.lista_servicios),
    path('proveedores', views.lista_proveedores),
    path('proveedores_2/<str:nombre_servicio>', views.lista_proveedores2),
    path('pagar_servicio', views.pagar_servicio),
]
