
from Usuarios import *
from Particular import *
from Profesional import *
from Comercial import *


class Clientes():

    def __init__(self):
        self.listaClientes = []

    def unParticular(self):
        print('ingrese datos cliente particular:')
        nom = input('nombre: ')
        dir = input('direccion: ')

        dni = input('dni: ')
        fechaNac = input('fecha de nacimiento: ')
        abo = 1
        unClienteParticular = Particular(nom, dir, abo, dni, fechaNac)
        return unClienteParticular

    def unProfesional(self):
        print('ingrese datos del cliente profesional:')
        nom = input('nombre: ')
        dir = input('direccion: ')
        abo = 2

        area = input('area: ')
        tit = input('titulo: ')
        unClienteProfesional = Profesional(nom, dir, abo, area, tit)
        return unClienteProfesional

    def unComercial(self):
        print('ingrese datos del cliente Comercial:')
        nom = input('nombre: ')
        dir = input('direccion: ')
        abo = 3

        rubro = input('rubro: ')
        cuit = input('cuit: ')
        unClienteComercial = Comercial(nom, dir, abo, rubro, cuit)
        return unClienteComercial

    def borraListado(self):
        print("Esta seguro que quiere borrar el listado?")
        # falta hacer alguna validacion
        opcion=self.continuar()
        if opcion == 1:
            self.listaClientes.clear()
    
    def continuar(self):
        seguir = 10
        while seguir != 0 or seguir != 1:
            print("Desea continuar: ")
            print("\t0- Volver ")
            print("\t1- Continuar: ")
            seguir = int(input("Ingresa tu eleccion: "))
            return seguir        
    
    def tipoUsuario(self):
        opc = 10
        print('Ingrese tipo de Cliente que desea crear: ')
        print('\t1. particular')
        print('\t2. profesional')
        print('\t3. comercial')
        print('\t0. volver')
        while opc < 0 or opc > 3:
            opc = int(input('ingrese opcion: '))
        return opc   
              
    def crearListado(self):
        print("Crear listado Clientes\n")
        seguir = 1
        tipoUsu = self.tipoUsuario()
        while(tipoUsu != -1):
            if tipoUsu == 1:
                while seguir != 0:
                    self.listaClientes.append(self.unParticular())
                    seguir = self.continuar()
                    if seguir == 0:
                        tipoUsu = -1
                        return tipoUsu

            elif tipoUsu == 2:
                while seguir != 0:
                    self.listaClientes.append(self.unProfesional())
                    seguir = self.continuar()
                    if seguir == 0:
                        tipoUsu = -1
                        return tipoUsu

            elif tipoUsu == 3:
                while seguir != 0:
                    self.listaClientes.append(self.unComercial())
                    seguir = self.continuar()
                    if seguir == 0:
                        tipoUsu = -1
                        return tipoUsu

            elif tipoUsu == 0:
                print("Saliste del menu")
                tipoUsu = -1
                return tipoUsu

    def mostrarListaClientes(self):
        print("Mostrar listado Clientes\n")
        if len(self.listaClientes) > 0:
            for i in self.listaClientes:
                i.muestra()
                print("------------------------")
            
            input("Pulsa una tecla para continuar..")
        else:
            print("La lista de clientes esta vacia")            
            
         

    def buscarCliente(self):
        print("Buscar Cliente\n")
        dni = input("Ingrese el numero de dni a buscar: ")
        for cliente in self.listaClientes:
            if dni == cliente.dni:
                cliente.muestra()
                return cliente

    def calcularImportes(self, unidades):
        Usuarios.calcularImportes(self, unidades)
        
    def salir(self):
        print("Gracias por utilizar Zaiken Aplications!")
        print("Hasta Luego!!")
        input("Presione una tecla")
        exit()
