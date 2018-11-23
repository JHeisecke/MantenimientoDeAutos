from abc import ABCMeta, abstractmethod
from vista_util import *

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
