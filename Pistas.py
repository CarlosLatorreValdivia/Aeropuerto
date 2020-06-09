class Pista:
	def __init__(self, nPista, tamano, disponibilidad=True):
		self.__nPista = nPista		
		self.__tamano = tamano
		self.__disponibilidad = disponibilidad

	@property
	def nPista(self):
		return self.__nPista

	@property
	def tamano(self):
		return self.__tamano

	@property
	def disponibilidad(self):
		return self.__disponibilidad

	@disponibilidad.setter
	def disponibilidad(self, disp):
		self.__disponibilidad = disp

	def __str__(self):
		return f"Pista: {self.nPista} {self.tamano:6}\t\t Disponible: {self.disponibilidad}"

	def __repr__(self):
		return f'Pista({self.nPista}, {self.tamano}, {self.disponibilidad})'

if __name__ == '__main__':
	p1 = Pista(1, 1)
	print(repr(p1))
	p2 = Pista(2, 1)
	print(p2)
	p2.disponibilidad = False
	print(p2)
	print(p1.tamano)
	print(p1.nPista)
