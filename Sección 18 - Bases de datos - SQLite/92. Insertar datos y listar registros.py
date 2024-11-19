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
conexion.commit()

# Insertar datos
cursor.execute("""
INSERT INTO productos VALUES (null, 'Primer Producto', 'Descripción de mi producto', 1500)
""")
conexion.commit()  # Se actualiza y guardan los datos

# Listar datos o consultas
cursor.execute("""
SELECT * FROM productos               
""")
productos = cursor.fetchall()
print(productos)

# Se ve mejor la información en vez de print(productos)
for producto in productos:
    print(productos)

for producto in productos:
    print("Título: ", producto[1])
    print("Descripción: ", producto[2])
    print("Precio: ", producto[3])
    print("\n")

# Obtener el primer registro de la tabla
cursor.execute("""
SELECT Titulo FROM productos
""")
producto = cursor.fetchone()
print(producto)

# Cerrar conexión
conexion.close()

print(f"Base de datos creada y guardada en: {ruta_bd}")