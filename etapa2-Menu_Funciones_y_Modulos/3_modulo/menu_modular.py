"""
Este archivo implementa un menú interactivo que importa un módulo
(`modulo_mini`) y hace uso de sus funciones. Las funciones invocadas
están implementadas en un archivo `.py` homónimo al nombre del módulo
(`modulo_mini.py`).
"""

import modulo_mini as modulo

def menu():
    while True:
        print("Menú:")
        print("1. Opción 1")
        print("2. Opción 2")
        print("3. Opción 3")
        print("4. Opción 4")
        print("5. Salir")
        
        opcion = input("Elija una opción: ")
        
        if opcion == "1":
            modulo.opcion1()
        elif opcion == "2":
            modulo.opcion2()
        elif opcion == "3":
            modulo.opcion3()
        elif opcion == "4":
            variableNombre = input('Ingresa tu nombre: ')
            modulo.opcion4(variableNombre)# se le pasa el valor a la funcion opcion4
        elif opcion == "5":
            print("Gracias por usar el programa")
            break
        else: 
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu()