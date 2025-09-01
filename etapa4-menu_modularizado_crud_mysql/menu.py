import baseDeDatos
import crudPersona
import crudCiudad

def mensajeBienvenida():
    print("***************************************************************************************************************")
    print("                                                                                                                ")
    print("***************         BIENVENIDOS AL CRUD DE PERSONAS Y CIUDADES DONDE NACIO CADA PERSONA   ******************")
    print("                                                                                                                ")
    print("***************************************************************************************************************")
    
def menu():
    while True:
        
        mensajeBienvenida()

        print("Menú:")
        print("1. Insertar Persona")
        print("2. Actualizar Persona")
        print("3. Eliminar Persona")
        print("4. Insertar Ciudad")
        print("5. Actualizar Ciudad")
        print("6. Eliminar Ciudad")
        print("7. Mostrar Todas las Personas")
        print("8. Mostrar Personas por Ciudad")
        print("9. Mostrar Personas segun filtro")    
        print("10. Buscar una Persona")    
        print("11. Mostrar Todas las Ciudades")
        print("12. Mostrar Ciudades por Provincia")
        print("13. Buscar una Ciudad")    
        print("14. Mostrar todas las personas y la ciudad donde nacieron")
        print("15. Salir")
        
        opcion = input("Elija una opción: ")
        
        if opcion == "1":
            crudPersona.insertar_persona()
        elif opcion == "2":
            crudPersona.actualizar_persona()
        elif opcion == "3":
            crudPersona.eliminar_persona()
        elif opcion == "4":
            crudCiudad.insertar_ciudad()
        elif opcion == "5":
            crudCiudad.actualizar_ciudad()
        elif opcion == "6":
            crudCiudad.eliminar_ciudad()
        elif opcion == "7":
            crudPersona.mostrar_todas_las_personas()
        elif opcion == "8":
            crudPersona.mostrar_personas_por_ciudad()
        elif opcion == "9":
            crudPersona.mostrar_personas_segun_filtro(input('Ingrese un filtro sobre la tabla Persona si lo desea (si no ingresa nada traerá todas las personas): '))
        elif opcion == "10":
            crudPersona.buscarPersona(input('Ingrese el ID de la Persona: '))
        elif opcion == "11":
            crudCiudad.mostrar_todas_las_ciudades()
        elif opcion == "12":
            crudCiudad.mostrar_ciudades_por_provincia()
        elif opcion == "13":
            crudCiudad.buscarCiudad(input('Ingrese el ID de la Ciudad: '))
        elif opcion == "14":
            crudPersona.mostrar_personas_y_ciudad_donde_nacio()        
        elif opcion == "15":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":    
    menu()
    
    # Cerrar cursor y conexión
    baseDeDatos.cerrarConexion()
