import shelve
import BaseDeDatos as bd

def guardarDatos(objeto,nombreArchivo, clave):
    ''' metodo o funcion que sirve para
     guardar los datos en basededatos'''
    try:
        basededatos = shelve.open(nombreArchivo,'n')
        basededatos[clave] = objeto
    except FileNotFoundError:
        print("Archivo no existe")

    else:
        basededatos.close()


# ---------------------------------------------------------------------------
"""funciones de cargar y guardar utilizado para
una mejor reutilizacion tanto por consola"""


def cargar_datos():
    '''carga los datos en listas para su uso'''
    bd.clientes = cargarLista("clientes", "Clientes")
    bd.asesores = cargarLista("asesores", "Asesores")


def guardar_datos():
    '''guarda los datos en las listas en archivos para la persistencia'''
    guardarDatos(bd.clientes,"Clientes", "clientes")
    guardarDatos(bd.asesores,"Asesores", "asesores")

# ---------------------------------------------------------------------------
def cargarLista(clave, nombreArchivo):
    '''carga los datos al sistema cuando
     cuando el sist. se ejecuta'''
    try:
        basededatos = shelve.open(nombreArchivo)
        lista = basededatos[clave]

        return lista

    except KeyError:
        return []
