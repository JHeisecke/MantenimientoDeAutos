from abc import ABCMeta, abstractmethod
from util import *

class Repuesto():

    def __init__(self, costo="", marca="", tipo="", **kwargs):
        super(Repuesto, self).__init__()
        self.costo=costo
        self.marca=marca
        self.tipo=tipo
        
    def prompt_init():
        """Se crea un diccionario con los claves y valores necesarios para
        instanciar al objeto"""
        tipo = input_opcion_repuesto("Ingrese un repuesto",("Faro", "Neumatico", "N/A"))
        if(tipo=="N/A"):
            costo = 0
            marca = "N/A"
        else:
            costo = input_entero("Ingrese costo")
            marca = input_string("Ingrese marca del repuesto").title()        
        return dict({
            "costo": costo,
            "tipo": tipo,
            "marca": marca,
        })
