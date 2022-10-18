from Usuarios import *
class Profesional(Usuarios):
    def __init__(self, nombre, direccion, abono, area, titulo):
        super().__init__(nombre,direccion,abono)
        self.__area=area
        self.__titulo=titulo
    
    #getters y setters:
    @property
    def area(self):
        return self.__area
    @area.setter
    def area(self,area):
        self.__area=area
        
    @property
    def titulo(self):
        return self.__titulo 
    @titulo.setter
    def titulo(self,titulo):
        self.__titulo=titulo

    #metodos:

    def calcularImportes(self,unidades):
        if unidades > 0 and unidades <= 200:
            totalPagar = unidades*0.07
        elif unidades > 200 and unidades <= 400:
            totalPagar = unidades * 0.11
        elif unidades > 400 and unidades <= 1000:
            totalPagar = unidades*0.13
        elif unidades > 1000:
            totalPagar = unidades*0.15
        return (print("Total a pagar: $", totalPagar))
    
    def muestra(self):
        super().muestra()
        print('area:',self.area)
        print('titulo:',self.titulo)

    