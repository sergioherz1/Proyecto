#from django.contrib import admin
from django.urls import path
#from django.conf.urls import include
from . import views

urlpatterns = [
    path('guardarPersona',views.guardarPersona),
    path('',views.index),
    path('nombre',views.nombre),
    path('sumar',views.sumar),
    path('esclava',views.esclava),
    path('consulta',views.consulta),
    path('modificar',views.modificar),
    path('editar',views.modificacion)
    #url(r'^',include('app.urls')),
   # path('admin/', admin.site.urls),
]