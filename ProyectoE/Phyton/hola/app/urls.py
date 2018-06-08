#from django.contrib import admin
from django.urls import path
#from django.conf.urls import include
from . import views

urlpatterns = [
    path('guardartrabajador',views.guardartrabajador),
    path('consulta/',views.consulta),
    path('index',views.index),
    path('trabajador',views.trabajador),
    path('modificar/', views.modificar),
    path('consulta/modificacion/', views.modificacion),
    path('eliminar', views.eliminar),
   
    #url(r'^',include('app.urls')),
   # path('admin/', admin.site.urls),
]