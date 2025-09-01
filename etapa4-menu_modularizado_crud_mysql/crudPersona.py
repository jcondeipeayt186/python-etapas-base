import baseDeDatos
import crudCiudad

def insertar_persona():
    #Datos para la nueva persona
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    dni = input("DNI: ")
    email = input("Email: ")
    fecha_nacimiento = input("Fecha de Nacimiento (AAAA-MM-DD): ")
    telefono = input("Teléfono: ")
    ciudad_id = input("ID de la Ciudad: ")
    
    #SQL sin los valores
    query = "INSERT INTO Persona (nombre, apellido, dni, email, fecha_nacimiento, telefono, ciudad_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    #valores que van a cargarse en el SQL de la inserción
    values = (nombre, apellido, dni, email, fecha_nacimiento, telefono, ciudad_id)
    
    baseDeDatos.cursor.execute(query, values)# Ejecuta el SQL (query) con los parametros (values) que se cargarán en orden en el SQL (query)
    baseDeDatos.conn.commit() #Es necesario realizar el commit(); de lo contrario, no se realizan cambios en la tabla 
    print("Persona insertada con éxito.")

def actualizar_persona():
    id_persona = input("ID de la Persona a actualizar: ")
    if(buscarPersona(id_persona)):
        nombre = input("Nuevo Nombre: ")
        apellido = input("Nuevo Apellido: ")
        dni = input("Nuevo DNI: ")
        email = input("Nuevo Email: ")
        fecha_nacimiento = input("Nueva Fecha de Nacimiento (AAAA-MM-DD): ")
        telefono = input("Nuevo Teléfono: ")
        ciudad_id = input("ID de Ciudad donde nacio: ")
        
        query = "UPDATE Persona SET nombre = %s, apellido = %s, dni = %s, email = %s, fecha_nacimiento = %s, telefono = %s, ciudad_id = %s WHERE id = %s"
        values = (nombre, apellido, dni, email, fecha_nacimiento, telefono, ciudad_id, id_persona)
        
        baseDeDatos.cursor.execute(query, values)
        baseDeDatos.conn.commit()
        print(f"Persona con ID {id_persona} actualizada con éxito.")
    else:
        print(f"Persona con ID {id_persona} NO EXISTE por lo tanto no puede ser modificada.")

def eliminar_persona():
    id_persona = input("ID de la Persona a eliminar: ")
    if(buscarPersona(id_persona)):
        query = "DELETE FROM Persona WHERE id = %s"
        values = (id_persona,)
        
        baseDeDatos.cursor.execute(query, values)
        baseDeDatos.conn.commit()
        print(f"Persona con ID {id_persona} eliminada con éxito.")
    else:
        print(f"Persona con ID {id_persona} NO EXISTE por lo tanto no puede ser eliminada.")

def mostrar_todas_las_personas():
    query = "SELECT * FROM Persona"
    baseDeDatos.cursor.execute(query)
    personas = baseDeDatos.cursor.fetchall()
    
    if personas:
        for persona in personas:
            print(persona)
    else:
        print("No hay personas en la base de datos.")

def mostrar_personas_por_ciudad():
    ciudad_id = input("ID de la Ciudad para mostrar personas: ")
    
    if(crudCiudad.buscarCiudad(ciudad_id)):
        query = "SELECT * FROM Persona WHERE ciudad_id = %s"
        values = (ciudad_id,)
        baseDeDatos.cursor.execute(query, values)
        personas = baseDeDatos.cursor.fetchall()
        
        if personas:
            print(f"Las personas que nacieron en la ciudad con id:{ciudad_id} son:")
            for persona in personas:
                print(persona)
        else:
            print(f"No hay personas en la Ciudad con ID {ciudad_id}.")
    else: 
        print(f"No existe la Ciudad con ID {ciudad_id}.")


def mostrar_personas_segun_filtro(filtro):
    #filtro puede venir vacio, en ese caso muestra todas las personas, sino viene algo asi como WHERE nombre = 'Juan'
    query = "SELECT id, nombre, apellido, dni FROM Persona "+filtro
    baseDeDatos.cursor.execute(query)
    personas = baseDeDatos.cursor.fetchall()

    print("////////////////////////mostrar_personas_segun_filtro//////////////////////")
    print(f"La consulta a la base de datos es: {query}")
    
    if personas:
        print(f"Hay {len(personas)} resultados, ellos son:.......")
        for persona in personas:
            print("--------------------------------")
            print(persona)
            print(f"El ID es {persona[0]}")
            print(f"El nombre es {persona[1]}")
            print(f"El apellido es {persona[2]}")
            print(f"El dni es {persona[3]}")
            print("--------------------------------")
    else:
        print("No hay personas en la base de datos.")
    
    print("//////////////////////////////////////////////////////////////////////////")


def buscarPersona(id):
    query = "SELECT * FROM Persona WHERE id = %s"
    values = (id,)
    baseDeDatos.cursor.execute(query,values)
    personaUnica = baseDeDatos.cursor.fetchone()

    print(baseDeDatos.cursor.rowcount, "Filas afectadas")

    if(baseDeDatos.cursor.rowcount == 1):
        print(personaUnica)
        return True
    else:
        print(f"No existe en la base de datos la persona con id: {id}")
        return False

    
# Consulta que involucre más de una tabla
def mostrar_personas_y_ciudad_donde_nacio():    
    query = "SELECT p.nombre, p.apellido, c.nombre FROM Persona as p, Ciudad as c WHERE p.ciudad_id = c.id"
    queryUtilizandoJoin = "SELECT p.nombre, p.apellido, c.nombre FROM Persona as p INNER JOIN Ciudad as c ON p.ciudad_id = c.id"
    query = queryUtilizandoJoin
    baseDeDatos.cursor.execute(query)
    resultado = baseDeDatos.cursor.fetchall()

    print("////////////////////////mostrar_personas_y_ciudad_donde_nacio//////////////////////")
    print(f"La consulta a la base de datos es: {query}")
    
    if resultado:
        print(f"Hay {len(resultado)} resultados, ellos son:.......")
        for fila in resultado:
            print("--------------------------------")
            print(fila)
            print(f"Nombre de la Persona {fila[0]}")
            print(f"Apellido de la Persona {fila[1]}")
            print(f"Nombre de la Ciudad {fila[2]}")
            print("--------------------------------")
            
    else:
        print("No hay personas relacionadas con ciudad en la base de datos.")
    
    print("//////////////////////////////////////////////////////////////////////////")

