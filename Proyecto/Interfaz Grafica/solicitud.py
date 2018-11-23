# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from datetime import datetime
from vehiculo import *
from repuesto import *
from vista_util import *
#________________________________SOLICITUD_____________________________________



class Boleta(metaclass=ABCMeta):
    '''Boleta es una clase abstracta'''
    @abstractmethod
    def __init__(self):
        pass
    
class Solicitud(Boleta):
    """Clase donde se guardan los datos de la solicitud de mantenimiento
    ---Se almacenan los datos de los vehiculos"""
    def __init__(self, fecha='' , cliente='', asesor='', vehiculo='', repuestos=''):
        super().__init__()
        self.fecha = fecha
        self.cliente = cliente
        self.asesor = asesor
        self.vehiculo=vehiculo
        self.repuestos= repuestos