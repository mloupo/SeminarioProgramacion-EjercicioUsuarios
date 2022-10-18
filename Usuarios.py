class Usuarios():
    def __init__(self, nombre, direccion, abono):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__abono = abono
        self.__baja = False
        

    # getters y setters
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def setNombre(self, nombre):
        self.__nombre = nombre

    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def setDireccion(self, direccion):
        self.__direccion = direccion

    @property
    def abono(self):
        return self.__abono

    @abono.setter
    def abono(self, abono):
        self.__abono = abono

    # metodos

    def calcularImportes(self):
        return ()

    def eliminar(self):
        self.__baja = True
        return self.__baja

    def muestra(self):
        print('nombre:', self.__nombre)
        print('direccion:', self.__direccion)
        print('abono:', self.__abono)

    def validar(self, miString):
        caracterBuscado="@"
        for c in miString:
            if c == caracterBuscado:
                return True
        return False