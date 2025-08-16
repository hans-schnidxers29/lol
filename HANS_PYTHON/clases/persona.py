class persona: 
    def __init__(self, nombre, apellido):
        self._nombre = nombre 
        self._apellido= apellido
        
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, new_nombre):
        self._nombre=new_nombre

