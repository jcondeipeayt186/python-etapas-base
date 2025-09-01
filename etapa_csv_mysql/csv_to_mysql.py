import pandas as pd
import mysql.connector

# =========================
# 1. Leer datos del CSV
# =========================
df = pd.read_csv("ejemplo_horarios/horariosMySQL.csv")  # Archivo con columnas: Hora, DiaSemana

# =========================
# 2. Conectar a MySQL
# =========================
conexion = mysql.connector.connect(
    host="localhost",      # Dirección del servidor MySQL
    user="COMPLETAR",     # Usuario MySQL
    password="COMPLETAR",# Contraseña
    database="COMPLETAR" # Nombre de la base de datos
)
cursor = conexion.cursor()

# =========================
# 3. Insertar datos en la tabla
# =========================
for index, row in df.iterrows():
    sql = "INSERT INTO horarios (Hora, DiaSemana) VALUES (%s, %s)"
    valores = (row["Hora"], row["DiaSemana"])
    cursor.execute(sql, valores)

# Confirmar cambios
conexion.commit()

print(f"✅ {len(df)} registros insertados en la tabla 'horarios'.")

# =========================
# 4. Cerrar conexión
# =========================
cursor.close()
conexion.close()
print("🔗 Conexión a MySQL cerrada.")

