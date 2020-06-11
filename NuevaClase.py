import TorreControl as tc
import Avion as av
import Pistas as p
import Aeropuerto as a 

a1 = a.Aeropuerto(4)
print(a1)
a1.agregarTorre('Charlie', 'Sur', 2)
print(a1.mostrarTorres())

#El metodo contratar cambia el estado de la torre de True a False
a1.contratar(a1.torres[0])
print(a1.mostrarTorres())
a1.contratar(a1.torres[0])

#El metodo agregarTorre crea un objeto de la clase TorreControl
a1.agregarTorre('Alpha', 'Sur', 8)
a1.agregarTorre('Alpha', 'Norte', 4)
a1.agregarTorre('Bravo', 'Este', 4)

av1 = av.Avion('Boeing 787', 3, 'Aeromexico', 'DE', 100, 700)
av2 = av.Avion('G-BXEX', 1, 'Aeromexico', 'CDMX', 2, 800)
av4 = av.Avion('3', 1, 'Aeromexico', 'CDMX', 90, 800)
av5 = av.Avion('5', 3, 'Aeromexico', 'CDMX', 150, 800)
av6 = av.Avion('6', 2, 'Aeromexico', 'DE', 5, 700)
av7 = av.Avion('7', 2, 'Aeromexico', 'CDMX', 90, 800)

a1.torres[0].agregarAviones([av1, av2, av5, av4, av6, av7])	
print(a1.mostrarTorres())

a1.torres[0].acomodarAviones()
print(a1.torres[0].esperando())
