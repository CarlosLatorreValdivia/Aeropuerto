import Pistas as land
import Avion as flug

class Hangar:
    def __init__(self, avion, pistas, disponible,tipoHangar):
        self.__avion = avion
        self.__pistas = pistas
        self.__disponible = disponible
        self.__tipoHangar = tipoHangar
        self.__avionesGuardados = []
    @property
    def avion(self):
        return self.__avion
    
    @avion.setter
    def avion(self):
        self.__avion = avion
    
    @property
    def pistas(self):
        return self.__pistas
    
    @property
    def disponible(self):
        return self.__disponible
    
    @disponible.setter
    def disponible(self):
        self.__disponible = disponible
    
    @property
    def tipoHangar(self):
        return self.__tipoHangar
    @property
    def avionesGuardados(self):
        return self.__avionesGuardados
    
        
    def orden(self):
        for avion in self.avion:
            if len(self.avionesGuardados) < 5 :
                 if self.tipoHangar == avion.tamano:
                     self.avionesGuardados.append(avion)
                     print('¡Avión guardado!')
        if len(self.avionesGuardados) == 1:
            print ('Un avión guardado')
        elif len(self.avionesGuardados) > 1:
            print (len(self.avionesGuardados),' aviones guardados.')
        return 'Hasta luego'
     
        
                
                                    
#if __name__ == '__main__':
    #a1 = flug.Avion('2', 1, 'Lufthansa', 'DE', 100, 700)
    #a2 = flug.Avion('1', 1, 'Aeromexico', 'CDMX', 150, 800)
    #a3 = flug.Avion('4', 2, 'Lufthansa', 'DE', 5, 700)
    #a4 = flug.Avion('3', 2, 'Mexicana', 'CDMX', 90, 800)
    #a5 = flug.Avion('3', 3, 'British Airways', 'CDMX', 90, 800)
    #a6 = flug.Avion('3', 3, 'Aeromexico', 'CDMX', 90, 800)
    #p1 = [land.Pista(1,1)]
    #hang = [a1,a2,a3,a4,a5,a6]
    #h = Hangar(hang,p1,True,1)
    #h2 = Hangar(hang,p1,True, 2)
    #h3 = Hangar(hang,p1,True, 3)
    #print(h.orden())
    #print(h2.orden())
    #print(h3.orden())
    
    
        