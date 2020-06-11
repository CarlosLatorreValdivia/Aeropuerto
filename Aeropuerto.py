'''
		Carlos Latorre Valdivia A01379354
'''

import TorreControl as tc


class Aeropuerto:
	def __init__(self, tamano, funcionamiento=True):
		self.__tamano = tamano
		self.__funcionamiento = funcionamiento
		self.__torres = []
		self.__ubicaciones = ''
		
	@property
	def tamano(self):
		return self.__tamano
		
	@property	
	def funcionamiento(self):
		return self.__funcionamiento

	@property
	def torres(self):
		return self.__torres

	@property
	def ubicaciones(self):
		return self.__ubicaciones

	@ubicaciones.setter
	def ubicaciones(self, ubi):
		self.__ubicaciones = ubi

	def agregarTorre(self, n, u, r):
		if u.upper() not in self.ubicaciones:
			self.torres.append(tc.TorreControl(n, u, r))
			self.ubicaciones += u.upper()
		else:
			print("Ya existe una torre ahi")

	def contratar(self, torre):
		if torre.operador == True:
			print("Ya hay alguien trabajando ahi")
		else:
			torre.operador = True

	def mostrarTorres(self):
		torres = '\n'
		for torre in self.torres:
			torres += str(torre) + '\n'
		return torres

	def __str__(self):
		return f'Aeropuerto tamano {self.tamano}\t Funcion: {self.funcionamiento}'
	


if __name__ == '__main__':
	a1 = Aeropuerto(2)
	print(a1)
	a1.agregarTorre('Charlie', 'Sur', 2)
	print(a1.mostrarTorres())
	a1.contratar(a1.torres[0])
	print(a1.mostrarTorres())
	a1.contratar(a1.torres[0])
	a1.agregarTorre('Alpha', 'Sur', 4)
	a1.agregarTorre('Alpha', 'Norte', 4)
