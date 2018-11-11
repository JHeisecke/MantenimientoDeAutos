from abc import ABCMeta, abstractmethod
from datetime import timedelta, datetime
from persona import Cliente, Asesor
from contacto import *
from util import *
from vehiculo import *
from repuesto import *
import base_de_datos as bd
import gestionador
from solicitud import Solicitud



class Empresa(metaclass=ABCMeta):
    '''Ficha es una clase abstracta'''
    @abstractmethod
    def __init__(self):
        pass

class LocalDeMantenimiento(Empresa):
    """Clase que contiene todos los menus y las funciones para modificar
    los datos del LocalDeMantenimiento"""
    def __init__(self, clientes=[], asesores=[], repuestos=[], solicitudes=[]):
        self.clientes=clientes
        self.asesores=asesores
        self.repuestos=repuestos
        self.solicitudes=solicitudes

#_______________________________________Asesores______________________________
    def add_asesor(self):
        """Se encarga de agregar el objeto Asesor a la base de datos y procede a guardar los datos para la persistencia de ellos"""
        cls()
        print("\n\n--==Ingrese los datos para el asesor==--\n")
        print("La fecha de inicio es igual a la fecha actual")
        bd.asesores.append(Asesor(**Asesor.prompt_init()))
        gestionador.guardar_datos()
        
    def del_asesor(self):
        """Se encarga de borrar el asesor seleccionado"""
        self.del_datos(bd.asesores)

#________________________________Menu___Cliente________________________________
    def add_cliente(self):
        """Se encarga de agregar el objeto Cliente a la base de datos y procede a guardar los datos para la persistencia de ellos"""
        cls()
        print("\n\n--==Ingrese los datos del cliente==--\n")
        bd.clientes.append(Cliente(**Cliente.prompt_init()))
        gestionador.guardar_datos()

    def del_cliente(self):
        """Se encarga de borrar el cliente seleccionado"""
        self.del_clientes(bd.clientes)

#_______________________________Menu___Solicitudes_____________________________
    def add_solicitud(self):
        """Se encarga de agregar el objeto Solicitud a la base de datos y procede a guardar los datos para la persistencia de ellos"""
        cls()
        print("\n\n--==Ingrese los datos de la solicitud==--\n")
        datos = Solicitud.promp_init()
        solicitud = Solicitud(**datos)
        bd.solicitudes.append(solicitud)
        gestionador.guardar_datos()
#_________________________________LISTADO_________________________________

    def del_datos(self, lista):
        """Permite eliminar un objeto por valor posicional del mismo"""
        if lista:
            pos = input_entero("Ingrese la posicion del dato a eliminar")
            if pos is not None:
                try:
                    #lista[pos - 1].mostrar_datos()
                    resp = input_opcion("Esta seguro?",
                    ("s", "n"))
                    if resp == "s":
                        lista.pop(pos - 1)
                        print("Eliminado.")
                    else:
                        print("Cancelado.")
                except ValueError:
                    print("ERROR valor incorrecto")
            else:
                print("Cancelado.")
        else:
            print("\nSin datos.")
        input("Presione enter para continuar...")


    def listar_asesores(self, p=True):
        """Permite listar los datos contenidos en los distintos vectores
           El valor p = False sirve para imprimir sin pausas"""
        numero = 1
        if bd.asesores:
            print()
            for val in bd.asesores:
                print(("-----------------==Detalles Asesores==-----------------".format(numero)))
                print("================")
                print(("Cedula: {}".format(val.cedula)))
                print(("Nombre: {}".format(val.nombre)))
                print(("Apellido: {}".format(val.apellido)))
                print(("Direccion: {}".format(val.direccion)))
                print(("Fecha de inicio: {}".format(val.fecha_ini)))
                print(("Sueldo: {}".format(val.sueldo)))
                print()
                print("\t---Detalle Contacto---")
                print("\tTel.: {}".format(val.contactos.tel))
                print("\tEmail: {}".format(val.contactos.email))
                numero += 1
            if p:
                input("Presione enter para volver al menu...")
        else:
            input("\nSin datos. \nPresione enter para continuar...")

    def listar_solicitudes(self, p=True):
        """Permite listar los datos contenidos en los distintos vectores
           El valor p = False sirve para imprimir sin pausas"""
        numero = 1
        if bd.solicitudes:
            print()
            for val in bd.solicitudes:
                print(("-----------------==Detalles Solicitudes==-----------------".format(numero)))
                print("================")
                print(("Fecha: {}".format(val.fecha)))
                print(("Cliente: {}".format(val.cliente)))
                print(("Asesor: {}".format(val.asesor)))
                print()
                print("\t---Detalle Vehiculo---")
                print("\tMarca: {}".format(val.vehiculo.marca))
                print("\tModelo: {}".format(val.vehiculo.modelo))
                print("\tChapa: {}".format(val.vehiculo.chapa))
                print()
                print("\t---Detalle Vehiculo---")
                print("\ttipo: {}".format(val.repuesto.tipo))
                print("\tmarca: {}".format(val.repuesto.marca))
                print("\tcosto: {}".format(val.repuesto.costo))
                print()
                numero += 1
            if p:
                input("Presione enter para volver al menu...")
        else:
            input("\nSin datos. \nPresione enter para continuar...")
            
    def listar_clientes(self, p=True):
        """Permite listar los datos contenidos en los distintos vectores
           El valor p = False sirve para imprimir sin pausas"""
        numero = 1
        if bd.clientes:
            print()
            for val in bd.clientes:
                print(("-----------------==Detalles Clientes==-----------------".format(numero)))
                print("================")
                print(("Cedula: {}".format(val.cedula)))
                print(("Nombre: {}".format(val.nombre)))
                print(("Apellido: {}".format(val.apellido)))
                print(("Direccion: {}".format(val.direccion)))
                print(("RUC: {}".format(val.ruc)))
                print()
                print("\t---Detalle Contacto---")
                print("\tTel.: {}".format(val.contactos.tel))
                print("\tEmail: {}".format(val.contactos.email))
                print()
                numero += 1
            if p:
                input("Presione enter para volver al menu...")
        else:
            input("\nSin datos. \nPresione enter para continuar...")
#______________________________________________________________________________
#___________________________________MENUS______________________________________

    def fin(self):
        """Funcion que guarda los datos agregados, imprime una despedida y cierra el programa"""
        gestionador.guardar_datos()
        print("\n\n----------Todos los datos fueron guardados----------------")
        print("\n-----------------------Adios!-----------------------------")
        exit()

    def menu_principal(self):
        """Menu principal del programa"""
        while True:
            cls()
            print("-----------------------------------------------------------")
            print("--------------------MENU PRINCIPAL------------------------")
            print()
            for key in list(self.opciones.keys()):
                print(("{} - {}".format(key, self.opciones[key]["clave"])))
            print()
            opcion = input_range("Ingrese una opcion", 1, len(self.opciones))
            if opcion=='':
                menu_principal()
            else:
                self.opciones[int(opcion)]["funcion"](self)
            

    def menu_dinamico(self, text, dic, tam):
        """Presenta el menu con las opciones"""
        while True:
            cls()
            print(("\n------------------{}--------------------------\n".
            format(text)))
            for key in list(dic.keys()):
                print(("{} - {}".format(key, dic[key]["clave"])))
            print()
            opcion = input_range("Ingrese una opcion", 1, tam)
            dic[int(opcion)]["funcion"](self)

    def fin(self):
        """Funcion que guarda los datos agregados, imprime una despedida y cierra el programa"""
        gestionador.guardar_datos()
        print("\n\n----------Todos los datos fueron guardados----------------")
        print("\n-----------------------Adios!-----------------------------")
        exit()

    def menu_clientes(self):
        """Esta funcion es utilizada para pasar los parametros propios de los clientes"""
        self.menu_dinamico("MENU CLIENTES", self.o_clientes, len(self.o_clientes))

    def menu_asesores(self):
        self.menu_dinamico("MENU ASESORES", self.o_asesores, len(self.o_asesores))

    def menu_repuestos(self):
        self.menu_dinamico("MENU REPUESTOS", self.o_repuestos, len(self.o_repuestos))

    def menu_solicitudes(self):
        self.menu_dinamico("MENU SOLICITUDES", self.o_solicitudes, len(self.o_solicitudes))

    opciones = {}
    opciones[1] = {"clave": "Menu de Cliente", "funcion": menu_clientes}
    opciones[2] = {"clave": "Menu de Asesores", "funcion": menu_asesores}
    opciones[3] = {"clave": "Menu de Repuestos", "funcion": menu_repuestos}
    opciones[4] = {"clave": "Menu de Solicitudes", "funcion": menu_solicitudes}
    opciones[5] = {"clave": "Salir", "funcion": fin}

    o_clientes= {}
    o_clientes[1] = {"clave": "Volver al menu principal", "funcion": menu_principal}
    o_clientes[2] = {"clave": "Agregar Cliente", "funcion": add_cliente}
    o_clientes[3] = {"clave": "Eliminar Cliente", "funcion": del_cliente}
    o_clientes[4] = {"clave": "Listar Clientes", "funcion": listar_clientes}
    o_clientes[5] = {"clave": "Salir", "funcion": fin}

    o_asesores = {}
    o_asesores[1] = {"clave": "Volver al menu principal", "funcion": menu_principal}
    o_asesores[2] = {"clave": "Agregar Asesor", "funcion": add_asesor}
    o_asesores[3] = {"clave": "Eliminar Asesor", "funcion": del_asesor}
    o_asesores[4] = {"clave": "Listar Asesores", "funcion": listar_asesores}
    o_asesores[5] = {"clave": "Salir", "funcion": fin}
    
    o_solicitudes = {}
    o_solicitudes[1] = {"clave": "Volver al menu principal", "funcion": menu_principal}
    o_solicitudes[2] = {"clave": "Agregar Solicitud", "funcion": add_solicitud}
    o_solicitudes[3] = {"clave": "Listar Solicitudes", "funcion": listar_solicitudes}
    o_solicitudes[4] = {"clave": "Salir", "funcion": fin}
    
    o_repuestos = {}
    o_repuestos[1] = {"clave": "Volver al menu principal", "funcion": menu_principal}
    #o_repuestos[2] = {"clave": "Agregar repuesto", "funcion": }
    o_repuestos[2] = {"clave": "Salir", "funcion": fin}
#______________________________________________________________________________
#______________________________________________________________________________
#______________________________________________________________________________

    def script_cargar_datos(self):
        """Funcion que sirve para cargar algunos datos en el sistema"""
        gestionador.cargar_datos()
        # bd.clientes.append(Cliente(ruc='', cedula=4500000, nombre="Juan",
        # apellido="Frans", direccion='San Lorenzo'))
        # bd.clientes[0].contactos = Contacto(tel='021 678678',
        # email='juan_f@hotmail.com')

        # bd.clientes.append(Cliente(ruc='', cedula=1678789, nombre="Juani",
        # apellido="Maidana", direccion='Luque'))
        # bd.clientes[1].contactos = Contacto(tel='021 545454',
        # email='juani_@gmail.com')

        # bd.clientes.append(Cliente(ruc='111111111-1', cedula=2345678,
        # nombre="Carlos", apellido="Enrique", direccion='San Lorenzo'))
        # bd.clientes[2].contactos = Contacto(tel='021 254652')

        # bd.clientes.append(Cliente(ruc='222222222-2', cedula=954789,
        # nombre="Arnaldo", apellido="Perez", direccion='Asuncion'))
        # bd.clientes[3].contactos = Contacto(tel='021 434343',
        # email='Arnaldo@gmail.com')

        # bd.clientes.append(Cliente(ruc='', cedula=4555555,
        # nombre="Mati", apellido="Kun", direccion='San Lorenzo'))
        # bd.clientes[4].contactos = Contacto(tel='09349846',
        # email='matipolo@gmail.com')

        # bd.clientes.append(Cliente(ruc='', cedula=4567890,
        # nombre="Romina", apellido="Rejala", direccion=''))
        # bd.clientes[5].contactos = Contacto(tel='021 8467412',
        # email='rom@gmail.com')

        # bd.asesores.append(Asesor(fecha_ini='', sueldo=2000000,
        # cedula=2912456, nombre="Lucia", apellido="Perez",
        # direccion='Asuncion'))
        # bd.asesores[0].contactos = Contacto(tel='0984123123',
        # email='Lucia@gmail.com')

        # bd.asesores.append(Asesor(fecha_ini='', sueldo=1500000,
        # cedula=2944456, nombre="Junior", apellido="Aguero",
        # direccion='San Lorenzo'))
        # bd.asesores[1].contactos = Contacto(tel='0983459844',
        # email='junior@gmail.com')

        # bd.asesores.append(Asesor(fecha_ini='', sueldo=3000000,
        # cedula=3912456, nombre="David", apellido="Guerrero",
        # direccion='San Lorenzo, casa: 90'))
        # bd.asesores[2].contactos = Contacto(tel='021 545454',
        # email='juani_@gmail.com')

        # bd.asesores.append(Asesor(fecha_ini='', sueldo=1500000,
        # cedula=2919956, nombre="Dani", apellido="Perez",
        # direccion='San Lorenzo'))
        # bd.asesores[3].contactos = Contacto(tel='0984123123',
        # email='Dani@gmail.com')

        # bd.asesores.append(Asesor(fecha_ini='', sueldo=1500000,
        # cedula=2915436, nombre="Julia", apellido="Espinoza",
        # direccion='San Lorenzo'))
        # bd.asesores[4].contactos = Contacto(tel='0981123456',
        # email='juli@gmail.com')

        # bd.asesores.append(Asesor(fecha_ini='', sueldo=6000000,
        # cedula=1912456, nombre="Pedro", apellido="Pedrinho",
        # direccion='Asuncion'))
        # bd.asesores[5].contactos = Contacto(tel='0975486941',
        # email='pedrito@gmail.com')
