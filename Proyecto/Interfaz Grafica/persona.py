# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from contacto import *
from vista_util import *
from datetime import datetime

#________________________________PERSONA_______________________________________

class Persona(metaclass=ABCMeta):
    '''Clase padre que permite crear a un objeto de tipo persona'''

    def __init__(self, cedula=0, nombre='', apellido='', direccion='',
    contacto=None, **kwargs):
        super().__init__(**kwargs)
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.contactos = contacto




#_____________________________CLIENTE_______________________________________

class Cliente(Persona):
    '''Clase extendida de Persona que detalla el ruc del cliente'''

    def __init__(self, ruc='N/A', **kwargs):
        super().__init__(**kwargs)
        self.ruc = ruc

#________________________________asesor______________________________________


class Asesor(Persona):
    '''Clase extendida de Persona que detalla al asesor'''

    def __init__(self, fecha_ini='', sueldo=0, **kwargs):
        super().__init__(**kwargs)
        self.fecha_ini = fecha_ini
        self.sueldo = sueldo

#______________________________________________________________________________
