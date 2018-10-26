# -*- coding: utf-8 -*-
import os
#________________________________Util__________________________________________
#Validadores para distintos casos y necesidades


def cls():
    """Permite limpiar la consola de python para que sea mas comodo usarla"""
    os.system('cls')

def input_opcion(text, opciones):
    """ Solicita un valor que debe estar presente en la lista opciones (no es requerido)"""
    text += " ({})*: ".format(", ".join(opciones))
    val = input(text)
    while val.lower() not in opciones:
        val = input(text)
    return val.lower()

def input_entero(text):
    """ Solicita un valor entero y lo devuelve. (es requerido)
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
            return valor
        except ValueError:
            print('ERROR no se acepta vacio')
            

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