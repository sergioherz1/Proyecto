#x= 10
#print ("Tipo es=", type(x))

#print ("hola mundo")
#nombre = input("Escribe tu nombre:  ")
#lista =[33,"cadena",True]         //lista
#print ("la lista tiene= ",lista) //

#tupla =(33,"cadena",True)
#print ("la lista tiene= ",tupla)

#diccionario ={"Oracle":"Solaris","Microsoft":"Windows"}
#print ("Oracle =", diccionario["Oracle"])

#letra ="a"
#if letra =="b":
#    print ("verdadero")
#    print("Dentro de verdadero")
#print ("fuera del IF")
#else:
#    print("falso")
#print("fuera del IF")

#import random
#num= random.randrange(-10,11,1)
#print("se obtuvo = ",num)
#if num>0:
#    print("positivo")
#elif num<0:
#    print("negativo")
#else:
#    print("neutro")

#import random
#num = random.randrange(20)
#print ("par") if num%2==0 else ("impar")

#ciclo while


#ciclo for
#for n in range(11):
#    print("N = ",n)

#metodo parametros
#def metodo(p1):
#    print("invocando metodo!",p1)
#metodo("metodo 1")
#metodo("hola")
#metodo("holax2")

#metodo con valor default
#def metodo(p1=33,p2="abc"):
# print ("parametro 1 ",p1)
# print ("parametro 2 ",p2)

#metodo(1)

#metodo con parametros tupla
#def metodo(p1=33,p2="abc",*otros):
#    print("paramatros 1",p1)
#    print("parametros 2",p2)
#    print("otros: ",otros)
#
#    metodo("p1","p2",1,2,3,4,5)

#
#def metodo(p1=33,p2="abc",**otros):
#    print("paramatros 1",p1)
#    print("parametros 2",p2)
#    print("otros: ",otros)
#
#metodo("p1","p2",p3=1,p4=2,nombre="felipe")

#def metodo(p1,lista):
#    print("parametro 1: ",p1)
#    print("parametro 2: ",lista)
#
#metodo(2,[1,2,3,4,5])

#metodos con retorno
#def suma2(n1,n2):
#    return n1+n2
#suma =suma2(3,4)
    
#print("la suma es: ", suma)

#metodo con retorno multiple
#def metodo(n1,n2):
#    return n1*2,n2*2
#r1,r2=metodo(2,3)
#print ("el resultado es: ",r1," y ",r2)

#clases y objetos
#class profesor:
#    def __init__(self):
#       self.clave=10
#       self.nombre="felipe"
#       print("iniciando objeto")
#    def mostrar(self):
#        print("Clave =", self.clave)
#        print("nombre =", self.nombre)
#
#p=profesor()
#p.mostrar()

#modificadores
#class clase:
#    def __privado(self):
#        print("metodo privado")
#    
#    def __init__(self):
#        self.clave=10
#        self.nombre="felipe"
#        print("iniciando objeto")
#    def mostrar(self):
#        print("Clave =", self.clave)
#        print("nombre =", self.nombre)
#        self.__privado()
#
#p=clase()
#p.mostrar()
#p.__privado()

#herencia
#class persona:
#    nombre=("")
#    def __init__(self,nomnre):
#        self.nombre=nombre

#class Profesor(persona):
#    clave=("")
#p1=persona("pepe")
#p2=persona("maria")
#print(p1.nombre)
#print(p2.nombre)

#from clases.persona import persona
#p= persona() 
