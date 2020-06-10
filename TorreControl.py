import Pistas as p
import Avion as av

class TorreControl:
	def __init__(self, nombre, ubicacion, rango, operador=False):
		self.__nombre = nombre
		self.__aviones = []
		self.__pistas = []
		self.__operador = operador
		self.__ubicacion = ubicacion
		self.__rango = rango
		self.__espera = []
		
	@property
	def nombre(self):
		return self.__nombre

	@property
	def aviones(self):
		return self.__aviones
	
	@property
	def pistas(self):
		return self.__pistas
	
	@property
	def operador(self):
		return self.__operador

	@property
	def ubicacion(self):
		return self.__ubicacion
	
	@property
	def rango(self):
		return self.__rango

	@property
	def espera(self):
		return self.__espera

	@operador.setter
	def operador(self, op):
		self.operador = op

	def autoPista(self):
		for i in range(0, self.rango):
			self.pistas.append(p.Pista(i+1, i//2 + 1))

	def agregarPista(self, pista):
		if len(self.pistas) < self.rango:
			self.pistas.append(pista)
		else:
			print('No mas pistas disponibles')
			
	def mostrarPistas(self):
		pistas = '\n'
		for pista in self.pistas:
			pistas += str(pista) + '\n'
		return pistas

	def agregarAviones(self, aviones):
		for avion in aviones:
			self.aviones.append(avion)

	def esperando(self):
		espera = '\nAviones en espera: \n'
		for e in self.espera:
			espera += str(e) + '\n'
		return espera

	def acomodarAviones(self):
		def ordenar(e):
			return e.pasajeros

		avionesAcomodados = []
		a3 = []
		a2 = []
		a1 = []
		for a in self.aviones:
			if a.tamano == 3:
				a3.append(a) 
			if a.tamano == 2:
				a2.append(a)
			if a.tamano == 1:
				a1.append(a)
		a3.sort(reverse=True, key=ordenar)
		a2.sort(reverse=True, key=ordenar)
		a1.sort(reverse=True, key=ordenar)
		for p in self.pistas:
			if p.disponibilidad == True:
				if p.tamano == 3:
					if len(a3) > 0:
						avionesAcomodados.append([a3[0], p])
						a3.remove(a3[0])
						p.disponibilidad = False
			if p.disponibilidad == True:
				if p.tamano == 2:
					if len(a2) > 0:
						avionesAcomodados.append([a2[0], p])
						a2.remove(a2[0])
						p.disponibilidad = False
			if p.disponibilidad == True:
				if p.tamano == 1:
					if len(a1) > 0:
						avionesAcomodados.append([a1[0], p])
						a1.remove(a1[0])
						p.disponibilidad = False
		for a in a3:
			self.espera.append(a)
			a.retraso = 30
		for a in a2:
			self.espera.append(a)
			a.retraso = 30
		for a in a1:
			self.espera.append(a)
			a.retraso = 30
		
		return avionesAcomodados		
			

	def __str__(self):
		return f"Torre {self.nombre} en {self.ubicacion}: {self.operador}\n\tRango: {self.rango}\n\tAviones: {len(self.aviones)}"

if __name__ == '__main__':
	t1 = TorreControl('Halcon', 'Norte', 6)
	t1.autoPista()
	print(t1)
	print(t1.mostrarPistas())
	a1 = av.Avion('2', 3, 'Aeromexico', 'DE', 100, 700)
	a2 = av.Avion('1', 3, 'Aeromexico', 'CDMX', 150, 800)
	a3 = av.Avion('4', 1, 'Aeromexico', 'DE', 5, 700)
	a4 = av.Avion('3', 1, 'Aeromexico', 'CDMX', 90, 800)
	a5 = av.Avion('5', 3, 'Aeromexico', 'CDMX', 150, 800)
	a6 = av.Avion('6', 2, 'Aeromexico', 'DE', 5, 700)
	a7 = av.Avion('7', 2, 'Aeromexico', 'CDMX', 90, 800)
	t1.agregarAviones([a1, a2, a3, a4, a5, a6, a7])
	a = t1.acomodarAviones()
	print(t1)
	print(t1.esperando())
	print(t1.mostrarPistas())