import os
#________________________________Util__________________________________________
#Validadores para distintos casos y necesidades


def cls():
    """Permite limpiar la consola de python para que sea mas comodo usarla"""
    os.system('cls')

def input_opcion(text, opciones):
    """ Recibe dos parametros: 'texto': que contiene un mensaje para el usuario 
        'opciones': es un tuple con s y n
    Solicita un valor que debe estar presente en la lista opciones"""
    text += " [{}]*: ".format("/".join(opciones))
    valor = input(text)
    while valor.lower() not in opciones:
        valor = input(text)
    return valor.lower()

def input_opcion_repuesto(text, opciones):
    """ Recibe dos parametros: 'texto': que contiene un mensaje para el usuario 
        'opciones': es un tuple con repuestos
    Solicita un valor que debe estar presente en la lista opciones"""
    text += " ({})*: ".format(",".join(opciones))
    valor = input(text)
    while valor not in opciones:
        valor = input(text)
    return valor	

def input_entero(text):
    """ Recibe un parametro: 'texto': que contiene un mensaje para el usuario
        Solicita un valor entero y lo devuelve.
        Mientras el valor ingresado no sea entero, vuelve a solicitarlo. """
    while True:
        valor = input("{}: ".format(text))
        try:
            valor = int(valor)
            return valor
        except ValueError:
            print('ERROR ingrese numeros')
            

def input_string(text):
    """ Recibe un parametro: 'texto': que contiene un mensaje para el usuario
        Solicita una cadena y no acepta valores vacios"""
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
    """Recibe un parametro: 'texto': que contiene un mensaje para el usuario
        Solicita una cadena para los casos donde no es requerida una repuesta"""
    while True:
        valor = input("{}: ".format(text))
        try:
            return valor
        except ValueError:
            pass
            

def input_range(text, men, may):
    """ Recibe tres parametros: 'texto': que contiene un mensaje para el usuario
        'men': indica el menor valor que sera posible para el usuario ingresar
        'may': el mayor valor que sra posible para el usuario ingresar
        Solicita un valor entero dentro de un rango y se retorna
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
