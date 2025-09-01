import mysql.connector

""" 
conn = mysql.connector.connect(
    host="localhost",
    user="tu_usuario",
    password="tu_contraseña",
    database="nombre_de_tu_base_de_datos"
)
"""

# Conectarse a la base de datos
#conn es una variable que contiene un objeto que representa la conexion a la base de datos.
conn = mysql.connector.connect(
    host="localhost",
    user="",#COMPLETAR
    password="",#COMPLETAR
    database=""#COMPLETAR
)

# Crear un cursor.
#cursor es una variable que contiene un objeto que permite ejecutar consultas y obtener resultados de la base de datos.
cursor = conn.cursor()

#cerrar_conexion es una funcion que cierra el cursor y la conexion a la base de datos.
#Es importante cerrar la conexion para liberar recursos y evitar errores.
def cerrar_conexion():
    # Cerrar cursor y conexión
    cursor.close()#cierra el cursor
    conn.close()#cierra la conexion


if __name__ == "__main__":
    print(conn)#imprime la conexion
    print("--------------------------------")
    print("Mostrar las bases de datos")
    print("--------------------------------")
    cursor.execute("SHOW DATABASES")#Esto es sql

    for x in cursor:
        print(x)

    cursor.execute("SHOW TABLES")
    print("--------------------------------")
    print("Mostrar las tablas")
    print("--------------------------------")

    for x in cursor:
        print(x)

    cerrar_conexion()#cierra la conexion
   
  
    
