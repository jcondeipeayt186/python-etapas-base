import baseDeDatos


def insertar_ciudad():
    nombre = input("Nombre de la Ciudad: ")
    provincia = input("Provincia: ")
    codigo_postal = input("Código Postal: ")
    
    query = "INSERT INTO Ciudad (nombre, provincia, codigo_postal) VALUES (%s, %s, %s)"
    values = (nombre, provincia, codigo_postal)
    
    baseDeDatos.cursor.execute(query, values)
    baseDeDatos.conn.commit()
    print("Ciudad insertada con éxito.")

def actualizar_ciudad():
    id_ciudad = input("ID de la Ciudad a actualizar: ")
    if(buscarCiudad(id_ciudad)):
        nombre = input("Nuevo Nombre de la Ciudad: ")
        provincia = input("Nueva Provincia: ")
        codigo_postal = input("Nuevo Código Postal: ")
        
        query = "UPDATE Ciudad SET nombre = %s, provincia = %s, codigo_postal = %s WHERE id = %s"
        values = (nombre, provincia, codigo_postal, id_ciudad)
        
        baseDeDatos.cursor.execute(query, values)
        baseDeDatos.conn.commit()
        print(f"Ciudad con ID {id_ciudad} actualizada con éxito.")
    else:
        print(f"Ciudad con ID {id_ciudad} NO EXISTE por lo tanto no puede ser actualizada.")

def eliminar_ciudad():
    id_ciudad = input("ID de la Ciudad a eliminar: ")
    if(buscarCiudad(id_ciudad)):
        query = "DELETE FROM Ciudad WHERE id = %s"
        values = (id_ciudad,)
        
        baseDeDatos.cursor.execute(query, values)
        baseDeDatos.conn.commit()
        print(f"Ciudad con ID {id_ciudad} eliminada con éxito.")
    else:
        print(f"Ciudad con ID {id_ciudad} NO EXISTE por lo tanto no puede ser eliminada.")

def mostrar_todas_las_ciudades():
    query = "SELECT * FROM Ciudad"
    baseDeDatos.cursor.execute(query)
    ciudades = baseDeDatos.cursor.fetchall()
    
    if ciudades:
        for ciudad in ciudades:
            print(ciudad)
    else:
        print("No hay ciudades en la base de datos.")

def mostrar_ciudades_por_provincia():
    provincia = input("Provincia para mostrar ciudades: ")
    
    query = "SELECT * FROM Ciudad WHERE provincia = %s"
    values = (provincia,)
    baseDeDatos.cursor.execute(query, values)
    ciudades = baseDeDatos.cursor.fetchall()
    
    if ciudades:
        for ciudad in ciudades:
            print(ciudad)
    else:
        print(f"No hay ciudades en la Provincia {provincia}.")

def buscarCiudad(id):
    query = "SELECT * FROM Ciudad WHERE id = %s"
    values = (id,)
    baseDeDatos.cursor.execute(query,values)
    ciudadUnica = baseDeDatos.cursor.fetchone()

    print(baseDeDatos.cursor.rowcount, "Filas afectadas")

    if(baseDeDatos.cursor.rowcount == 1):
        print(ciudadUnica)
        return True
    else:
        print(f"No existe en la base de datos la ciudad con id: {id}")
        return False
