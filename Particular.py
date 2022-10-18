from Usuarios import *
class Particular(Usuarios):
    def __init__(self, nombre, direccion, abono, dni, fechaNacimiento):
        super().__init__(nombre,direccion,abono)
        self.__dni=dni
        self.__fechaNacimiento=fechaNacimiento
    
    #getters y setters:
    @property
    def dni(self):
        return self.__dni
    @dni.setter
    def dni(self,dni):
        self.__dni = dni

    @property
    def fechaNacimiento(self):
        return self.__fechaNacimiento
    @fechaNacimiento.setter
    def setFechaNacimiento(self,fechaNacimiento):
        self.__fechaNacimiento=fechaNacimiento

    #metodos:    
    def calcularImportes(self,unidades):
            if unidades > 0 and unidades <= 200:
                totalPagar = unidades*0.05
            elif unidades > 200 and unidades <= 400:
                totalPagar = unidades * 0.07
            elif unidades > 400 and unidades <= 1000:
                totalPagar = unidades*0.1
            elif unidades > 1000:
                totalPagar = unidades*0.12
            return (print("Total a pagar: $", totalPagar))

    def muestra(self):
        super().muestra()
        print('dni:',self.__dni) # revisar si lo muestra
        print('fecha de nacimiento:',self.__fechaNacimiento)

