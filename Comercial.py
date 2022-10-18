from Usuarios import *


class Comercial(Usuarios):
    def __init__(self, nombre, direccion, abono, rubro, cuit):
        super().__init__(nombre, direccion, abono)
        self.__rubro = rubro
        self.__cuit = cuit

    # getters y setters:
    @property
    def rubro(self):
        return self.__rubro

    @rubro.setter
    def rubro(self, rubro):
        self.__rubro = rubro

    @property
    def cuit(self):
        return self.__cuit

    @cuit.setter
    def cuit(self, cuit):
        self.__cuit = cuit

    # metodos:

    def calcularImportes(self, unidades):
        if unidades > 0 and unidades <= 200:
            totalPagar = unidades*0.09
        elif unidades > 200 and unidades <= 400:
            totalPagar = unidades * 0.12
        elif unidades > 400 and unidades <= 1000:
            totalPagar = unidades * 0.15
        elif unidades > 1000:
            totalPagar = unidades * 0.17
        return (print("Total a pagar: $", totalPagar))
    
    def muestra(self):
        super().muestra()
        print('rubro:', self.rubro)
        print('cuit:', self.cuit)
