# -*- coding: utf-8 -*-
from vista_util import *
from abc import ABCMeta, abstractmethod

#________________________________vehiculo_______________________________________

class MedioDeTransporte(metaclass=ABCMeta): 
	@abstractmethod
	def __init__(self):
		pass

class Vehiculo(MedioDeTransporte):
    '''Clase que contiene a los vehiculos para hacer mantenimiento de una solicitud'''

    def __init__(self, tipo='', marca='', modelo='', chapa=''):
        super(Vehiculo, self).__init__()
        self.marca = marca
        self.modelo = modelo
        self.chapa = chapa
#______________________________________________________________________________
