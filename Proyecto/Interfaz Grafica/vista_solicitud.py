# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox
import base_de_datos as bd
from solicitud import Solicitud
from vehiculo import Vehiculo
from repuesto import Repuesto
from datetime import timedelta, datetime
import gestionador
from functools import reduce

class AddSoli(PanedWindow):
	"Panel que contiene los campos para introducir los datos de la solicitud"

	cliente_entry = None
	asesor_entry = None
	tipo_entry = None
	marcaR_entry = None
	costo_entry = None
	marcaV_entry = None
	modelo_entry = None
	chapa_entry = None

	def __init__(self, panel_master):
		PanedWindow.__init__(self, master=panel_master)
		self.__panel_master = panel_master
		self.inicializar()
		self.pack()

	def inicializar(self):
		self.repuestos = []
		Label(self, text="Ingrese datos de la solicitud", ).grid(
			row=1, column=2)
		Label(self, text="Cliente*: ").grid(row=2, column=1)
		Label(self, text="Asesor*: ").grid(row=3, column=1)
		Label(self, text="Vehiculo*: ").grid(row=4, column=1)
		Label(self, text="Chapa*: ").grid(row=5, column=2)
		Label(self, text="Marca*: ").grid(row=6, column=2)
		Label(self, text="Modelo*: ").grid(row=7, column=2)
		Label(self, text="Repuestos*: ").grid(row=8, column=1)
		Label(self, text="Tipo*: ").grid(row=9, column=2)
		Label(self, text="Marca*: ").grid(row=10, column=2)
		Label(self, text="Costo*: ").grid(row=11, column=2)
		Button(self, text="Add Repuesto", command=self.agregar_repuesto).grid(
			row=12, column=2)
		Button(self, text="GUARDAR", command=self.agregar_solicitud).grid(
			row=13, column=1)

		self.get_cliente_entry()
		self.get_asesor_entry()
		self.get_tipo_entry()
		self.get_marcaR_entry()
		self.get_modelo_entry()
		self.get_marcaV_entry()
		self.get_costo_entry()
		self.get_chapa_entry()

	def get_cliente_entry(self):
		if not self.cliente_entry:
			self.cliente_entry = Entry(master=self, width=20)
			self.cliente_entry.grid(row=2, column=2)
		return self.cliente_entry

	def get_asesor_entry(self):
		if not self.asesor_entry:
			self.asesor_entry = Entry(master=self, width=20)
			self.asesor_entry.grid(row=3, column=2)
		return self.asesor_entry

	def get_tipo_entry(self):
		if not self.tipo_entry:
			self.tipo = StringVar()
			self.tipo_entry = Radiobutton(self, text="Faro",
				value="faro", variable=self.tipo)
			self.tipo_entry.grid(row=5, column=2)
			self.tipo_entry = Radiobutton(self, text="Neumatico",
				value="neumatico", variable=self.tipo)
			self.tipo_entry.grid(row=5, column=3)
			self.tipo_entry = Radiobutton(self, text="Espejos",
				value="espejos", variable=self.tipo)
			self.tipo_entry.grid(row=5, column=4)
			self.tipo_entry = Radiobutton(self, text="Otro",
				value="otro", variable=self.tipo)
			self.tipo_entry.grid(row=5, column=6)
		return self.tipo

	def get_marcaR_entry(self):
		if not self.marcaR_entry:
			self.marcaR_entry = Entry(master=self, width=20)
			self.marcaR_entry.grid(row=6, column=2)
		return self.marcaR_entry

	def get_modelo_entry(self):
		if not self.modelo_entry:
			self.modelo_entry = Entry(master=self, width=20)
			self.modelo_entry.grid(row=7, column=2)
		return self.modelo_entry

	def get_marcaV_entry(self):
		if not self.marcaV_entry:
			self.marcaV_entry = Entry(master=self, width=20)
			self.marcaV_entry.grid(row=6, column=2)
		return self.marcaV_entry

	def get_chapa_entry(self):
		if not self.chapa_entry:
			self.chapa_entry = Entry(master=self, width=20)
			self.chapa_entry.grid(row=2, column=2)
		return self.chapa_entry 

	def get_costo_entry(self):
		if not self.costo_entry:
			self.costo_entry = Entry(master=self, width=20)
			self.costo_entry.grid(row=10, column=2)
		return self.costo_entry

	def val_soli(self, c, e):
		val = False
		if c.isalpha() and e.isalpha():
			val = True
		else:
			messagebox.showinfo("", "Ingrese cliente y asesor")
		return val

	def agregar_solicitud(self):
			# Anhade la solicitud a la bd
			if self.repuestos:
				try:
					cli = self.get_cliente_entry().get()
					asesor = self.get_asesor_entry().get()
					if self.val_soli(cli, asesor):
						solicitud = Solicitud(**{"fecha": datetime.now(),
						"cliente": cli, "asesor": asesor})
						solicitud.repuesto = self.repuestos
						bd.solicitudes.append(solicitud)
						#print("final de ingreso de datos")
						messagebox.showinfo("Informacion", "Solicitud agregada")
						self.destroy()
				except Exception as e:
					messagebox.showerror('Error', e)
			else:
				messagebox.showinfo("Informacion", "Debe ingresar repuestos")

	def validar_repuesto(self, tip, mar, cos):
		val = False
		if tip != "" and mar != "" and (cos.isdigit() or cos == ""):
			val = True
		else:
			messagebox.showinfo("", "Ingrese correctamente los datos del " +
				"repuesto")
		return val

	def agregar_repuesto(self):
			try:
				tip = self.get_tipo_entry().get()
				mar = self.get_marcaR_entry().get()
				cos = self.get_costo_entry().get()
				if self.validar_repuesto(tip, mar, cos,):
					repuesto = Repuesto(**{"tipo": tip, "marca": mar,
					"costo_m": cos})
					self.repuestos.append(repuesto)
					messagebox.showinfo("Informacion", "Repuesto agregado")
			except Exception as e:
				messagebox.showerror('Error', e)