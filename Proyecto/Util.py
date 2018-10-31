import os
#________________________________Util__________________________________________
#Validadores para distintos casos y necesidades


def cls():
    """Permite limpiar la consola de python para que sea mas comodo usarla"""
    os.system('cls')

def input_opcion(text, opciones):
    """ Solicita un valor que debe estar presente en la lista opciones (no es requerido)"""
    text += " [{}]*: ".format("/".join(opciones)) #opciones es un tuple con s y n
    valor = input(text)
    while valor.lower() not in opciones:
        valor = input(text)
    return valor.lower()


def input_entero(text):
    """ Solicita un valor entero y lo devuelve.
        Mientras el valor ingresado no sea entero, vuelve a solicitarlo. """
    while True:
        valor = input("{}: ".format(text))
        try:
            valor = int(valor)
            return valor
        except ValueError:
            print('ERROR ingrese numeros')
            

def input_string(text):
    """ Solicita una cadena (requerido)"""
    while True:
        valor = input("{}: ".format(text))
        try:
            if valor is not '':
                return valor
            else:
                raise (ValueError)
        except ValueError:
            print('ERROR no se acepta vacio')

def input_string_norequerido(text):
    """Solicita una cadena para los casos donde no es requerida una repuesta"""
    while True:
        valor = input("{}: ".format(text))
        try:
            return valor
        except ValueError:
            pass
            

def input_range(text, men, may):
    """ Solicita un valor entero dentro de un rango y se devuelve
        Se introduce el texto a mostrar y el rango de valor minimo y maximo"""
    while True:
        valor = input("{} ({}-{}): ".format(text, men, may))
        try:
            valor = int(valor)
            if (valor <= may and valor >= men):
                return valor
            else:
                raise(ValueError)
        except ValueError:            
            print('ERROR ingrese un numero dentro del rango')
#______________________________________________________________________________