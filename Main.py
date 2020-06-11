import TorreControl as tc
import Avion as av
import Pistas as p


#Crea torre de control de la siguiente manera
#TorreControl(nombre:str, ubicacion:str, rango:int)
t1 = tc.TorreControl('Halcon', 'Norte', 6)

#Crea objetos avion de la siguiente manera
#Avion(nombre:str, tamano, int, aerolinea:str, destino:str, pasajeros:int, horario:int) 
a1 = av.Avion('1', 3, 'Aeromexico', 'DE', 100, 700)
a2 = av.Avion('2', 3, 'Aeromexico', 'CDMX', 10, 800)
a3 = av.Avion('3', 1, 'Aeromexico', 'US', 60, 700)
a4 = av.Avion('4', 1, 'Aeromexico', 'UK', 90, 800)
a5 = av.Avion('5', 3, 'Aeromexico', 'JP', 200, 800)
a6 = av.Avion('6', 2, 'Aeromexico', 'AU', 46, 700)
a7 = av.Avion('7', 2, 'Aeromexico', 'CA', 130, 800)

#El metodo agregar aviones agrega aviones a la lista de aviones de la torre
t1.agregarAviones([a1, a2, a3, a4, a5, a6, a7]) #Para este objeto se envia una lista de objetos de la clase avion

#Crea objeto pista de la siguiente manera
#Pista(numeroPista:int, tamano:int)
p1 = p.Pista(1, 1) 

t1.autoPista() #Este metodo crea automaticamente todas las pistas que acepta la torre de control

t1.agregarPista(p1) #Este metodo agrega una pista a la torre de control siempre y cuando haya espacio para ella
#Se le envia un objeto del tipo pista

#El metodo mostrarPistas imprime como str cada una de las pistas con sus respectivos nombres, tamanos y estados
print(t1.mostrarPistas())

#El siguiente metodo acomoda un avion en cada pista, dando prioridad a los aviones con mayor numero de pasajeros
t1.acomodarAviones() #Agrega los aviones sin pista a una espera y los retrasa
#Las pistas de tamano n solo pueden tener aviones de tamano n

#Este metodo regresa una lista de los aviones en espera
print(t1.esperando())

