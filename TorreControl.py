import Pistas as p


class TorreControl:
	def __init__(self, nombre, ubicacion, rango, operador=False):
		self.__nombre = nombre
		self.__aviones = []
		self.__pistas = []
		self.__operador = operador
		self.__ubicacion = ubicacion
		self.__rango = rango
		for i in range(0, rango):
			self.__pistas.append(p.Pista(i+1, i//2 + 1))

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

	def mostrarPistas(self):
		pistas = '\n'
		for pista in self.pistas:
			pistas += str(pista) + '\n'
		return pistas

	def __str__(self):
		return f"Torre {self.nombre} en {self.ubicacion}: {self.operador}\n\tRango: {self.rango}\n\tAviones: {len(self.aviones)}"

if __name__ == '__main__':
	t1 = TorreControl('Halcon', 'Norte', 6)
	print(t1)
	print(t1.mostrarPistas())
