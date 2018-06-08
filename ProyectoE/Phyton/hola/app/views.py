from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

from . import models
 # Create your views here.
def index(request):
   return render(request,'menu.html')
#TRABAJADORES
def trabajador(request):
   return render(request,'trabajador.html')

def paquetes(request):
    return render(request,'Paquetes.html')


def guardartrabajador(request):
    if 'idtrabajador' in request.POST and 'nombre' in request.POST and 'telefono' in request.POST and 'edad'in request.POST and 'Direccion' in request.POST:
        idtrabajador = request.POST['idtrabajador']
        nombre = request.POST['nombre']
        telefono = request.POST['telefono']
        edad = request.POST['edad']
        Direccion = request.POST['Direccion']
        t = models.trabajadores(idtrabajador = idtrabajador,nombre = nombre,telefono = telefono,edad = edad,Direccion = Direccion)
        t.save()
        return render(request,'Trabajadores.html',{'msg': 'Registro realizado corretamente'})
    else:
        return render(request,'Trabajadores.html',{'msg': 'no se puede realizar el registros'})
def consulta(request):
    registros = models.trabajadores.objects.all()
    return render(request,'consultatrab.html',{"registros":registros}) 


def modificacion(request):
    if 'idtrabajador' in request.POST:
        registro = models.trabajadores.objects.get(idtrabajador=request.POST['idtrabajador'])
        return render(request,'trabajadoresmod.html',{"reg":registro})
    else:
        return redirect('consultatrab.html/')

def modificar(request):
    if 'idtrabajador' in request.POST and 'nombre' in request.POST and 'telefono' in request.POST and 'edad' in request.POST and 'Direccion' in request.POST:
        p = models.trabajadores(idtrabajador = request.POST['idtrabajador'])
        p.nombre=request.POST['nombre']
        p.telefono=request.POST['telefono']
        p.edad=request.POST['edad']
        p.Direccion=request.POST['Direccion']
        
        p.save()
    return redirect('/hola/consulta', {'op':'Actualizacion Realizada'})

def eliminar(request):
    if 'idtrabajador' in request.POST:
        per = models.trabajadores.objects.get(idtrabajador=request.POST['idtrabajador'])
        per.delete()
    return redirect('/hola/consulta')