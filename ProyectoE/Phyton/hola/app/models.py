from __future__ import unicode_literals

from django.db import models

#Create your models here
    #COMANDO PARA PROBAR QUE ESTO FUNCIONE
    #python manage.py check app
class trabajadores(models.Model):
    idtrabajador=models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    edad = models.IntegerField()
    Direccion = models.CharField(max_length=50)

class paquetes(models.Model):
    idpaq=models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    Descripcion = models.CharField(max_length=50)

class inventario(models.Model):
    idinven=models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    status = models.CharField(max_length=50)


class contratos(models.Model):
    id_con=models.IntegerField(primary_key=True)
    Nombre_persona = models.CharField(max_length=50)
    Dirección = models.CharField(max_length=50)
    Telefono = models.IntegerField()
    Fecha = models.IntegerField()
    id_paq_id = models.ForeignKey(paquetes,on_delete=models.CASCADE)