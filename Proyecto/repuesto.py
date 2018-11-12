from abc import ABCMeta, abstractmethod
from util import *

costo_adicional=30000


class Provision(metaclass=ABCMeta): 
	@abstractmethod
	def __init__(self):
		pass

class Repuesto(Provision):

	def __init__(self, costo=0, marca="", tipo="", **kwargs):
		super(Repuesto, self).__init__()
		self.costo=costo
		self.marca=marca
		self.tipo=tipo
		
	def prompt_init():
		"""Se crea un diccionario con los claves y valores necesarios para
		instanciar al objeto"""
		tipo = input_opcion_repuesto("Ingrese un repuesto",("Faro", "Neumatico", "Espejo", "Otro"))
		if(tipo=="Otro"):
			tipo = input_string("Ingrese el tipo de repuesto")
			costo = input_entero("Ingrese costo")		
			costo+=costo_adicional
		else:
			costo = input_entero("Ingrese costo")
			
		marca = input_string("Ingrese marca del repuesto").title()		
		return dict({
			"costo": costo,
			"tipo": tipo,
			"marca": marca,
		})
