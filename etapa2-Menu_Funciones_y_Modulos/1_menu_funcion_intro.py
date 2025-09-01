def funcion1():
    while True:
        print("Menú:")
        print("1. Opción 1")
        print("2. Opción 2")
        print("3. Opción 3")
        print("4. Opción 4")
        print("5. Salir")
        
        opcion = input("Elija una opción: ")
        
        if opcion == "1":
            print("Eligio la opcion 1 ")
        elif opcion == "2":
            print("Eligio la opcion 2 ")
        elif opcion == "3":
            print("Eligio la opcion 3 ")
        elif opcion == "4":
            variableNombre = input('Ingresa tu nombre: ')
            print(f"Eligio la opcion 4: Hola {variableNombre}!!!")
        elif opcion == "5":
            print("Gracias por usar el programa")
            break
        else: 
            print("Opción no válida. Intente nuevamente.")




if __name__ == "__main__":
    funcion1()