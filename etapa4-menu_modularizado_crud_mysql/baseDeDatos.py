import mysql.connector

# Conectarse a la base de datos
conn = mysql.connector.connect(
    host="localhost",
    user="",#COMPLETAR
    password="",#COMPLETAR
    database=""#COMPLETAR
)

# Crear un cursor
cursor = conn.cursor()

def cerrarConexion():
    cursor.close()
    conn.close()