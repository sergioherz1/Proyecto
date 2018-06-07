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

#CONTRATOS

def consulta_Paquetes(request):
    registrosP = models.persona.objects.all()
    return render(request,'Consultar_Paquetes.html')

def modificacion_Paquetes(request):
    if 'idPaquete' in request.POST:
        registrosP = models.persona.objects.get(idPaquete=request.POST['idPaquete'])  
        return render(request,'Modificar_Paquetes.html',{'reg':registrosP})
    else:
        return redirect(request,'consultar_Paquets.html')

def editar_Paquetes(request):
    if 'idPaquete' in request.POST:
        per = models.persona.objects.get(idPaquete=request.POST['idPaquete'])
        return render(request,'Modificar_Paquetes.html',{'reg':per})
    else:
        return redirect('Consultar_Paquetes.html')
    
    def modificar_Paquetes(request):
        if 'idPaquete' in request.POST and 'nombre' in request.POST and 'costo' in request.POST and 'descripcion' in request.POST:
            p = models.persona(idPaquete = request.POST['idPaquete'])
            p.nombre = request.POST['nombre']
            p.costo = request.POST['costo']
            p.descripcion['descripcion']
            p.save
        return redirect('Consultar_Paquetes.html'.{'op':'Actualizacion realizada'})