
"""
Este archivo es un módulo de Python que expone únicamente funciones.
Las funciones definidas aquí pueden ser utilizadas desde otros archivos
mediante su importación y posterior invocación, por ejemplo:

    import modulo_mini
    modulo_mini.opcion1()

    # o bien
    from modulo_mini import opcion1
    opcion1()

"""


def opcion1():
    # Código de la opción 1
    print("Estoy en el archivo modulo_mini.py")
    print("Eligio la opcion 1 ")
    pass

def opcion2():
    # Código de la opción 2
    print("Eligio la opcion 2 ")
    pass

def opcion3():
    # Código de la opción 3
    print("Eligio la opcion 3 ")
    pass

""" Esta funcion es una funcion que recibe un valor como parametro y lo imprime """
def opcion4(valor):
    # Código de la opción 4
    print(f"Eligio la opcion 4: Hola {valor}!!!")
    pass

def funcion_no_expuesta():
    print("Funcion que no debe invocarse")

if __name__ == "__main__":#Modulo mini
    funcion_no_expuesta()