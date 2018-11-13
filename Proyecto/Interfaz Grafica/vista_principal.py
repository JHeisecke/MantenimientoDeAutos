# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox
from vista_util import *
from vista_solicitud import *
from vista_cliente import *
from vista_asesor import *
import gestionador


bgC = "black"
p_sal_pri = "700x400+150+100"
p_sal_sec = "500x300+250+180"

#______________________________________________________________________________
#________________________________Panel Principal_______________________________


class PanelPrincipal(Frame):
	"""Panel principal que contiene el menu con las llamadas a las funciones
	del programa"""
	__vista_actual = None

	def __init__(self, panel_master):
		Frame.__init__(self, panel_master)
		self.__panel_master = panel_master
		self.inicializar()
		self.script_cargar_datos()
		self.pack()

	def inicializar(self):
		self.__panel_master.geometry(p_sal_pri)
		self.__panel_master.title("MENU PRINCIPAL")
		self.__panel_master.protocol("WM_DELETE_WINDOW", "onexit")
		self.__panel_master.resizable(0, 0)
		self.__panel_master.config(bg=bgC)
		menubar = Menu(self.__panel_master)
		self.__panel_master.config(menu=menubar)

		menu_cliente = Menu(menubar, tearoff=0)
		menu_cliente.add_command(label="Agregar cliente",
			command=self.add_cliente)
		menu_cliente.add_command(label="Eliminar cliente",
			command=self.del_cliente)
		menu_cliente.add_command(label="Listar clientes", command=list_cliente)
		menubar.add_cascade(label="Clientes", menu=menu_cliente)

		menu_asesor = Menu(menubar, tearoff=0)
		menu_asesor.add_command(label="Agregar Asesor",
			command=self.add_asesor)
		menu_asesor.add_command(label="Eliminar Asesor",
			command=self.del_asesor)
		menu_asesor.add_command(label="Listar Asesor",
			command=list_asesor)
		menubar.add_cascade(label="Asesores", menu=menu_asesor)
		
		menu_ayuda = Menu(menubar, tearoff=0)
		menu_ayuda.add_separator()
		menu_ayuda.add_command(label="Acerca del sistema", command=self.info)
		menu_ayuda.add_separator()
		menubar.add_cascade(label="Ayuda", menu=menu_ayuda)

		menubar.add_command(label="Salir", command=self.salir)

#______________________________________________________________________________
#______________________________________________________________________________

	def salir(self):
		if(messagebox.askyesno("Salir", "Desea terminar la ejecucion?")):
			#self.quit()
			gestionador.guardar_datos()
			exit()

	def limpiar(self):
		if self.__vista_actual:
			self.__vista_actual.destroy()

	def info(self):
		messagebox.showinfo("Informacion","\n Info Temporal \n")
#______________________________________________________________________________
#______________________________________________________________________________
# Funciones que llaman los distintos frames para modificar los datos

	def add_cliente(self):
		self.limpiar()
		form = AddCliente(self.__panel_master)
		self.__vista_actual = form

	def del_cliente(self):
		self.limpiar()
		form = DelCliente(self.__panel_master)
		self.__vista_actual = form

	def add_asesor(self):
		self.limpiar()
		form = AddAsesor(self.__panel_master)
		self.__vista_actual = form

	def del_asesor(self):
		self.limpiar()
		form = DelAsesor(self.__panel_master)
		self.__vista_actual = form

#____________________________CARGAR__DATOS_____________________________________
#Script que se ejecuta para cargar algunos datos
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

		# bd.asesoreses.append(Asesor(fecha_ini='', sueldo=2000000,
		# cedula=2912456, nombre="Lucia", apellido="Perez",
		# direccion='Asuncion'))
		# bd.asesoreses[0].contactos = Contacto(tel='0984123123',
		# email='Lucia@gmail.com')

		# bd.asesoreses.append(Asesor(fecha_ini='', sueldo=1500000,
		# cedula=2944456, nombre="Junior", apellido="Aguero",
		# direccion='San Lorenzo'))
		# bd.asesoreses[1].contactos = Contacto(tel='0983459844',
		# email='junior@gmail.com')

		# bd.asesoreses.append(Asesor(fecha_ini='', sueldo=3000000,
		# cedula=3912456, nombre="David", apellido="Guerrero",
		# direccion='San Lorenzo, casa: 90'))
		# bd.asesoreses[2].contactos = Contacto(tel='021 545454',
		# email='juani_@gmail.com')

		# bd.asesoreses.append(Asesor(fecha_ini='', sueldo=1500000,
		# cedula=2919956, nombre="Dani", apellido="Perez",
		# direccion='San Lorenzo'))
		# bd.asesoreses[3].contactos = Contacto(tel='0984123123',
		# email='Dani@gmail.com')

		# bd.asesoreses.append(Asesor(fecha_ini='', sueldo=1500000,
		# cedula=2915436, nombre="Julia", apellido="Espinoza",
		# direccion='San Lorenzo'))
		# bd.asesoreses[4].contactos = Contacto(tel='0981123456',
		# email='juli@gmail.com')

		# bd.asesoreses.append(Asesor(fecha_ini='', sueldo=6000000,
		# cedula=1912456, nombre="Pedro", apellido="Pedrinho",
		# direccion='Asuncion'))
		# bd.asesoreses[5].contactos = Contacto(tel='0975486941',
		# email='pedrito@gmail.com')
