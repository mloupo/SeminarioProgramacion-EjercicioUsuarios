from Usuarios import *
from Particular import *
from Profesional import *
from Comercial import *
from Clientes import *


cli = Clientes()



while True:
    print("Menu principal del programa")
    print("Ingrese la operacion que desea realizar")
    print("\t1- Cargar Nuevo Cliente")
    print("\t2- Mostrar listado de Clientes")
    print("\t3- Calcular Total a Pagar x Cliente")
    print("\t4- Eliminar listado Clientes")
    print("\t5- Buscar Cliente")
    print("\t0- Fin Programa")
    opcion = int(input('ingrese opcion: '))

    if opcion == 1:
        opcion = cli.crearListado()

    elif opcion == 2:
        opcion = cli.mostrarListaClientes()
        
    elif opcion == 3:
        cliente= cli.buscarCliente()
        unid=int(input("Ingresa unidades:"))
        print("\t")
        cliente.calcularImportes(unid)
        
    elif opcion ==4:
        opcion=cli.borraListado()
        
    elif opcion == 5:
        cliente = cli.buscarCliente()
              
    elif opcion==0:       
        cli.salir()