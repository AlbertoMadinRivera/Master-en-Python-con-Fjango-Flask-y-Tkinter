import mysql.connector

# Conexión a la base de datos
database = mysql.connector.connect(
    host="localhost",       # Corregido: 'host' en lugar de 'hots'
    user="root",            # Usuario por defecto en XAMPP
    passwd="",              # Contraseña en blanco por defecto en XAMPP
#    database="master_python"  # El nombre de la base de datos que quieres usar
)

# Cómo saber que la conexión fue correcta?
print(database)

cursor = database.cursor()

cursor.execute("""
    CREATE DATABASE IF NOT EXISTS master_python
""")

# Al revisar dentro de mysql se observa, ahora solo falta revisar con código
cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd) # Se observa la que hemos creador que es ('master_python',)

"""
    Ahora ya podemos revisar la base de datos dentro de la conexión que hemos creado
"""

import mysql.connector

# Conexión a la base de datos
database = mysql.connector.connect(
    host="localhost",       # Corregido: 'host' en lugar de 'hots'
    user="root",            # Usuario por defecto en XAMPP
    passwd="",              # Contraseña en blanco por defecto en XAMPP
    database="master_python"  # El nombre de la base de datos que quieres usar
)
print(database)