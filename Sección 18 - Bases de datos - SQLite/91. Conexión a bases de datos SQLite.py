import sqlite3
import os

# Definir la ruta de la base de datos
ruta_bd = r"C:\\Users\\alber\\Universidad Autónoma Metropolitana\\Programming Project - Documentos\\General\\Master en Python con Fjango, Flask y Tkinter\\Sección 18 - Bases de datos - SQLite\\pruebas.db"

# Asegurarnos de que el directorio existe
os.makedirs(os.path.dirname(ruta_bd), exist_ok=True)

# Conexión a SQL
conexion = sqlite3.connect(ruta_bd)  # Fichero de la base de datos que se guardará en la ruta especificada

# Crear cursor
cursor = conexion.cursor()

# Crear tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos (
    ID INTEGER PRIMARY KEY AUTOINCREMENT, 
    Titulo TEXT, 
    Descripcion TEXT, 
    Precio INTEGER
)
""")

# Guardar cambios 
"""
Esto guarda todos los cambios dentro de la consulta
"""
conexion.commit()

# Cerrar conexión
conexion.close()

print(f"Base de datos creada y guardada en: {ruta_bd}")