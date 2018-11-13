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

    def prompt_init():
        """Se crea un diccionario con los indices y valores necesarios para
        instanciar al objeto"""
        return dict({
            "modelo": input_string("Marca del vehiculo"),
            "chapa": input_string("Modelo"),
            "marca": input_string("Chapa")
        })
    prompt_init = staticmethod(prompt_init)
#______________________________________________________________________________
