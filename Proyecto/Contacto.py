# -*- coding: utf-8 -*-
from util import *

#________________________________CONTACTO______________________________________#


class Contacto():
    '''Clase que contiene los contactos de las personas'''

    def __init__(self, tel='', email='N/A'):
        super(Contacto, self).__init__()
        self.tel = tel
        self.email = email

    def mostrar_datos(self):
        '''Permite mostrar los valores de los contactos'''
        print("\t---Detalle Contacto---")
        print("\tTel.: {}".format(self.tel))
        print("\tEmail: {}".format(self.email))

    def prompt_init():
        """Se crea un diccionario con las claves y valores necesarios para
        instanciar al objeto"""
        return dict({
            "tel": input_entero("Tel."),
            "email": input_string_norequerido("Ingrese email")})
    prompt_init = staticmethod(prompt_init)

#_____________________________________________________________________________
