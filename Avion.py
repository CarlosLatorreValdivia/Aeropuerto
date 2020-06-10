class Avion:
    def __init__(self,modelo,tamano,aerolinea,destino,pasajeros,tipo):
        self.__modelo = modelo
        self.__tamano = tamano
        self.__aerolinea = aerolinea
        self.__destino = destino
        self.__pasajeros = pasajeros
        self.__tipo = tipo
        
    @property
    def plane_Complete(self):
        return f'El tipo de avión es un {modelo} con un tamaño de {tamano} de la aerolínea, con destino a {destino}. Contiene {pasajeros}.'
    
    @property
    def volando(self):
        return f'El avión se ecnuentra en vuelo.'
    
    
    @property
    def despegar(self):
        return f'El avión con destino a {destino} está listo para despegar.'
    
    
    @property
    def aterrizar(self):
        return f'El avión con destino a {destino} se prepara para aterrizar.'
    
    
    @property
    def esperar(self):
        return f' El avión con destino a {destino} se encuentra en espera.'
    
    @property
    def plane_Type(self,tipo):
        if (tipo =='Carga') or (tipo == 'carga'):
            return f'El tipo de avión es un avión de carga. No transporta pasajeros'
        else:
            return f'El tipo de avión es de transporte de pasajeros'
    
    
    @property
    def abordaje(self):
        return f'El avión se encuentra en abordaje.'
    
    
    @property
    def desembarque(self):
        return f'El avión está desembarcando.'
    
    