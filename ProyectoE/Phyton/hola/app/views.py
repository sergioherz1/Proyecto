from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from . import persona
from . import models
 # Create your views here.
def index(request):
   return render(request,'menu.html')



#TRABAJADORES
def trabajador(request):
   return render(request,'trabajador.html')

def guardartrabajador(request):
    if 'idPersona' in request.POST and 'nombre' in request.POST and 'telefono' in request.POST and 'edad'in request.POST and 'direccion' in request.POST:  
      idPersona = request.POST['idPersona']
      nombre = request.POST['nombre']
      telefono=request.POST['telefono'] 
      edad = request.POST['edad']
      direccion=request.POST['direccion'] 
      p = models.persona(idPersona = idPersona,nombre = nombre,telefono=telefono,edad=edad,direccion=direccion)
      p.save()
      return render(request,'Trabajadores.html',{'msg': 'Registro realizado corretamente'})
    else:
        return render(request,'Trabajadores.html',{'msg': 'no se pudo realizar el registros'})
def consulta(request):
    registros = models.persona.objects.all()
    return render(request,'consultatrab.html',{"registros":registros}) 