# -*- coding: utf-8 -*-
from Util import *

#________________________________CONTACTO______________________________________#


class Contacto():
    '''Clase que contiene los contactos de las personas'''

    def __init__(self, tel='', email=''):
        super(Contacto, self).__init__()
        self.tel = tel
        self.emails = []
        self.emails.append(email)

    def get_tel(self):
        return self.tel

    def get_email(self):
        return self.emails

    def set_tel(self, tel=''):
        self.tel = tel

    def mostrar_datos(self):
        '''Permite mostrar los valores de los contactos'''
        print("\t---Detalle Contacto---")
        print("\tTel.: {}".format(self.tel))
        for mail in self.emails:
            print("\tEmail: {}".format(mail))

    def prompt_init():
        """Se crea un diccionario con las claves y valores necesarios para
        instanciar al objeto"""
        return dict({
            "tel": input_entero("Tel."),
            "email": input_string_norequerido("Ingrese email")})
    prompt_init = staticmethod(prompt_init)

#_____________________________________________________________________________
