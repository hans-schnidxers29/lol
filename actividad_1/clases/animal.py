class animal:
    def __init__(self,nombre, peso, propietario, fechaCumple, fechaUltimaVacuna):
        self._nombre = nombre
        self._propietario = propietario
        self._fechaCumple = fechaCumple
        self._fechaUltimaVacuna= fechaUltimaVacuna
        self._peso = peso
        
    @property
    def nombre(self):
        return self._nombre
    @property
    def fechaUltimaVacuna(self):
        return self._fechaUltimaVacuna
    @property
    def fechaCumple(self):
        return self._fechaCumple
    @property
    def peso(self):
        return self._peso
    @property
    def propietario(self):
        return self._propietario
    
    @nombre.setter
    def nombre(self,new_nombre):
        self._nombre = new_nombre
        
    @fechaCumple.setter
    def fechaCumple(self,cumplenuevo):
        self._fechaCumple = cumplenuevo

    @peso.setter
    def peso(self, pesonuevo):
        self._peso = pesonuevo
    
    @propietario.setter
    def propietario(self,nuevopropietario):
        self._propietario = nuevopropietario
    
    @fechaUltimaVacuna.setter
    def fechaUltimaVacuna(self, nuevafechavacuna):
        self._fechaUltimaVacuna= nuevafechavacuna 
    
    
    