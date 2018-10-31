# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from contacto import *
from util import *
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

    @abstractmethod
    def mostrar_datos(self):
        pass

    def prompt_init():
        """Se crea un diccionario con los claves y valores necesarios para
        instanciar al objeto"""
        return dict(cedula=input_entero('Ingrese cedula'),
            nombre=input_string('Ingrese nombre').title(),
            apellido=input_string('Ingrese apellido').title(),
            direccion=input_string('Ingrese direccion'))
    prompt_init = staticmethod(prompt_init)



#_____________________________CLIENTE_______________________________________

class Cliente(Persona):
    '''Clase extendida de Persona que detalla el ruc del cliente'''

    def __init__(self, ruc='N/A', **kwargs):
        super().__init__(**kwargs)
        self.ruc = ruc

    def get_ruc(self):
        return self.ruc

    def mostrar_datos(self):
        '''Sobreescribimos un metodo heredado'''
        print("\nDetalles Persona")
        print("================")
        print(("Cedula: {}".format(self.cedula)))
        print(("Nombre: {}".format(self.nombre)))
        print(("Apellido: {}".format(self.apellido)))
        print(("Direccion: {}".format(self.direccion)))
        print(("RUC: {}".format(self.ruc)))
        print()
        self.contactos.mostrar_datos()

    def prompt_init():
        """Se crea un diccionario con las claves y valores necesarios para
        instanciar al objeto"""
        persona = Persona.prompt_init()
        ruc = input_string_norequerido("RUC")
        datos = Contacto.prompt_init()
        contacto = Contacto(**datos)
        persona.update({
            "ruc": ruc,
            "contacto": contacto})

        return persona
    prompt_init = staticmethod(prompt_init)

#________________________________asesor______________________________________


class Asesor(Persona):
    '''Clase extendida de Persona que detalla al asesor'''

    def __init__(self, fecha_ini='', sueldo=0, **kwargs):
        super().__init__(**kwargs)
        self.fecha_ini = fecha_ini
        self.sueldo = sueldo

    def get_fecha_ini(self):
        return self.fecha_ini

    def get_sueldo(self):
        return self.sueldo

    def mostrar_datos(self):
        '''Sobreescribimos un metodo heredado'''
        print("\nDetalles Persona")
        print("================")
        print(("Cedula: {}".format(self.cedula)))
        print(("Nombre: {}".format(self.nombre)))
        print(("Apellido: {}".format(self.apellido)))
        print(("Direccion: {}".format(self.direccion)))
        print(("Fecha de inicio: {}".format(self.fecha_ini)))
        print(("Sueldo: {}".format(self.sueldo)))
        print()
        self.contactos.mostrar_datos()

    def prompt_init():
        """Se crea un diccionario con las claves y valores necesarios para
        instanciar al objeto"""
        persona = Persona.prompt_init()
        print("La fecha de inicio es igual a la fecha actual")
        fecha_ini = datetime.now()
        sueldo = input_entero("Ingrese sueldo")
        datos = Contacto.prompt_init()
        contacto = Contacto(**datos)
        persona.update({
            "fecha_ini": fecha_ini,
            "sueldo": sueldo,
            "contacto": contacto})
        return persona
    prompt_init = staticmethod(prompt_init)
#______________________________________________________________________________







# x[0] = Cliente(asfsdf)
# x[1] = Asesor(asdfasfja)

# for x in xrange(1,10):
#     x.prompt_init