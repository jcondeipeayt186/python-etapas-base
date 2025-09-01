import pandas as pd

# =========================
# Lectura de archivo CSV
# =========================
# El archivo 'horarios.csv' debe estar en la misma carpeta que este script
# y contener las columnas: Hora y DiaSemana
df = pd.read_csv("horarios.csv")

# =========================
# Mostrar el DataFrame completo
# =========================
print("📋 Datos completos del CSV:")
print(df)

# =========================
# Acceder a columnas completas
# =========================
# Acceder a la columna "Hora"
print("\n⏰ Columna Hora:")
print(df["Hora"])

# Acceder a la columna "DiaSemana"
print("\n📅 Columna DiaSemana:")
print(df["DiaSemana"])

# =========================
# Acceder a filas por índice
# =========================
# Primera fila (índice 0)
print("\n🔹 Primera fila completa (índice 0):")
print(df.iloc[0])

# Segunda fila (índice 1)
print("\n🔹 Segunda fila completa (índice 1):")
print(df.iloc[1])

# =========================
# Acceder a un valor específico
# =========================
# Ejemplo: Hora de la primera fila
hora_primera = df.iloc[0]["Hora"]
print(f"\n⏱ Hora en la primera fila: {hora_primera}")

# Ejemplo: Día de la semana de la tercera fila
dia_tercera = df.iloc[2]["DiaSemana"]
print(f"📆 Día en la tercera fila: {dia_tercera}")

# =========================
# Recorrer el DataFrame fila por fila
# =========================
print("\n🔄 Recorrido de todas las filas:")
for index, row in df.iterrows():
    print(f"Fila {index}: Hora={row['Hora']} - Día={row['DiaSemana']}")
