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
        self.repuestos= []

    def promp_init():
        """Se crea un diccionario con los indices y valores necesarios para
        instanciar al objeto"""
        fecha = datetime.now()
        print("La fecha de la solicitud es la actual")
        cliente=input_entero("Ingrese la cedula del cliente*")
        asesor=input_entero("Ingrese la cedula del asesor*")
        datosV = Vehiculo.prompt_init()
        vehiculo= Vehiculo(**datosV)    
        return dict({
            "fecha": fecha,
            "cliente": cliente,
            "asesor": asesor,
            "vehiculo": vehiculo
        })