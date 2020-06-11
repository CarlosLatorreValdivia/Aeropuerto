'''
		Carlos Latorre Valdivia A01379354
		Eduardo Aguilar Chias A01749375
'''

class Avion:
	def __init__(self, modelo, tamano, aerolinea, destino, pasajeros, horaSalida):
		self.__modelo = modelo
		self.__tamano = tamano
		self.__aerolinea = aerolinea
		self.__destino = destino
		self.__pasajeros = pasajeros
		self.__horaSalida = horaSalida
		self.__retraso = 0

	@property
	def modelo(self):
		return self.__modelo

	@property
	def tamano(self):
		return self.__tamano

	@property
	def aerolinea(self):
		return self.__aerolinea
	
	@property
	def destino(self):
		return self.__destino

	@property
	def pasajeros(self):
		return self.__pasajeros

	@property
	def horaSalida(self):
		return self.__horaSalida

	@property 
	def retraso(self):
		return self.__retraso

	@retraso.setter
	def retraso(self, ret):
		self.__retraso = ret

	def aterrizar(self):
		return f'El vuelo de {self.__modelo} con destino a {self.__destino} ha aterrizado'

	def despegar(self):
		return f'El vuelo de {self.__modelo} con destino a {self.__destino} ha despegado'

	def abordar(self):
		return f'{self.pasajeros} pasajeros han abordado'

	def desistir(self):
		return f'{self.pasajeros} pasajeros han salido'

	def esperar(self, tiempo):
		return f'El avion dirigido a {self.destino} esperara {tiempo} minutos'

	def __str__(self):
		return f'({self.modelo}, {self.tamano}, {self.pasajeros}) dirigido a {self.destino} a las {self.horaSalida} tiene {self.retraso} minutos de retraso'

if __name__ == '__main__':
	a1 = Avion('Boeing 787', 3, 'Aeromexico', 'DE', 100, 700)
	a2 = Avion('G-BXEX', 1, 'Aeromexico', 'CDMX', 2, 800)	
	print(a1)
	print(a1.modelo)
	print(a2.tamano)
	print(a1.retraso)
	a1.retraso = 60
	print(a1.retraso)