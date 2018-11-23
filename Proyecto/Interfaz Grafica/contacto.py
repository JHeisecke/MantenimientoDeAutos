# -*- coding: utf-8 -*-
from vista_util import *

#________________________________CONTACTO______________________________________#


class Contacto():
    '''Clase que contiene los contactos de las personas'''

    def __init__(self, tel='', email='N/A'):
        super(Contacto, self).__init__()
        self.tel = tel
        self.email = email

#_____________________________________________________________________________
