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

# Crear tabla si no existe
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
INSERT INTO productos (Titulo, Descripcion, Precio) VALUES ('Primer Producto', 'Descripción de mi producto', 1500)
""")
conexion.commit()  # Se actualiza y guardan los datos

# Listar datos o consultas
cursor.execute("""
SELECT * FROM productos               
""")
productos = cursor.fetchall()
print("Productos en la base de datos:")
for producto in productos:
    print(f"Título: {producto[1]}")
    print(f"Descripción: {producto[2]}")
    print(f"Precio: {producto[3]}")
    print("\n")

# Obtener el primer registro de la tabla
cursor.execute("""
SELECT Titulo FROM productos
""")
producto = cursor.fetchone()
print(f"Primer producto: {producto[0]}")

print("\n")

"""
    Borrar registros y actualizar registros dentro de python
"""

# Borrar todos los registros
cursor.execute("DELETE FROM productos")
conexion.commit()  # Confirmar que los cambios se han hecho

# Verificar que los productos han sido eliminados
cursor.execute("SELECT * FROM productos")
productos_borrados = cursor.fetchall()
print(f"Productos después de borrar: {productos_borrados}")

# Insertar muchos registros de golpe
productos = [
    ("Ordenador portatil", "PC Gamer", 1300),
    ("Teléfono inteligente", "Marca apple", 5000),
    ("Casa", "Casa de doble piso con 3 habitaciones", 300000),
    ("Carro", "Carro deportivo", 85000)
]

# Insertar registros múltiples sin el valor None para el ID
cursor.executemany("INSERT INTO productos (Titulo, Descripcion, Precio) VALUES (?, ?, ?)", productos)
conexion.commit()

# Verificar que los productos se han insertado correctamente
cursor.execute("SELECT * FROM productos")
productos_insertados = cursor.fetchall()
print(f"Productos después de insertar varios registros: {productos_insertados}")
print("\n")

# Cerrar conexión
conexion.close()

print(f"Base de datos creada y guardada en: {ruta_bd}")