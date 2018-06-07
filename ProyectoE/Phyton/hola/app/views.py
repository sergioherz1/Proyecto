from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from . import persona
from . import models
 # Create your views here.

def index(request):
   return render(request,'index.html')

def nombre(request):
    return HttpResponse("felipe jaimes liberato      I LOVE MADARA")

def nombre(request):
    valores= range(10)
    p = persona.Persona()
    p.iniciar(1,'felipe')
    p2 = persona.Persona()
    p2.iniciar(2,'felpex2')

    personas = [p,p2]

    return render(request,'nombre.html',{'personas':personas})

def esclava(request):
    return render(request,'esclavo.html')

def sumar(request):
    if 'num1' in request.POST and 'num2' in request.POST:  
      n1 = request.POST['num1']
      n2 = request.POST['num2']
      if len(n1)<=0 and len(n2)<=0:
          return render(request,'esclavo.html')
      suma = int(n1) + int(n2)
      return render(request,'esclavo.html',{'suma':suma,'num1':n1,'num2':n2})
    else:
        return render(request,'esclavo.html')

def guardarPersona(request):
    if 'idPersona' in request.POST and 'nombre' in request.POST and 'edad'in request.POST:  
      idPersona = request.POST['idPersona']
      nombre = request.POST['nombre']
      edad = request.POST['edad']
      p = models.persona(idPersona = idPersona,nombre = nombre,edad=edad)
      p.save()
      return render(request,'regPersona.html',{'msg': 'Registro realizado corretamente'})
    else:
        return render(request,'regPersona.html',{'msg': 'no se puede realizar el registros'})

def consulta(request):
    registros = models.persona.objects.all()
    return render(request,'consulta.html',{"registros":registros})     

def modificacion(request):
      if 'idPersona' in request.POST:
         registro = models.persona.objects.get(idPersona=request.POST['idPersona'])
         return render(request,'modificacion.html',{"reg":registro})
      else:
          return redirect('consulta.html')
def editar(request):
    if 'idPersona' in request.POST:
        per = models.persona.objects.get(idPersona=request.POST['idPersona'])
        return render(request,'modificacion.html',{'reg':per})
    else:
        return redirect('consulta')
def modificar (request):
    if 'idPersona' in request.POST and 'nombre' in request.POST and 'edad' in request.POST:
       p = models.persona(idPersona = request.POST['idPersona'])
       p.nombre = request.POST ['nombre']
       p.edad = request.POST['edad']
       p.save
    return redirect('consulta.html',{'op':'Actualizacion realizada'})