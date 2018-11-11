import shelve
import base_de_datos as bd

def cargar_datos():
    '''carga los datos en listas para su uso'''
    bd.clientes = cargar_lista("clientes", "Clientes")
    bd.asesores = cargar_lista("asesores", "Asesores")
    bd.solicitudes = cargar_lista("solicitudes", "Solicitudes")

def guardar_datos():
    '''guarda los datos en las listas en archivos para la persistencia'''
    guardar_lista(bd.clientes,"Clientes", "clientes")
    guardar_lista(bd.asesores,"Asesores", "asesores")
    guardar_lista(bd.solicitudes,"Solicitudes", "solicitudes")

    
# ---------------------------------------------------------------------------
def cargar_lista(clave, nombreArchivo):
    '''carga los datos al sistema cuando se este ejecutando'''
    try:
        basededatos = shelve.open(nombreArchivo)
        lista = basededatos[clave]
    
        if lista is None:
            lista = []


        return lista

    except KeyError:
        return print("ERROR Ocurrio un al encontrar los datos")

def guardar_lista(objeto,nombreArchivo, clave):
    ''' funcion que sirve para guardar los datos en basededatos'''
    try:
        basededatos = shelve.open(nombreArchivo,'n')
        basededatos[clave] = objeto
    except FileNotFoundError:
        print("ERROR Archivo no existe")

    else:
        basededatos.close()