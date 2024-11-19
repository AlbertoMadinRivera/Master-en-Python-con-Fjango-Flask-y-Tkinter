print("""
    Proyecto Python MySQL:
    - Abrir un asistente
    - Login o registro
    - Si elegimos registro, creará un usuario a la bbdd
    - Si se elige login, identificará al usuario y nos preguntará
    - Creará notas, mostrar notas, borrar notas
""")

# Trabajaremos con la base de datos creada anteriormente
# "master_python"

# Importamos las acciones para los usuarios
from usuarios import acciones

print("""
Acciones disponibles:
      1. Registro
      2. Login
""")

haz_El = acciones.Acciones()
accion = input("¿Qué deseas realizar? (Escribe el número o la opción): ")

# Asegúrate de manejar la entrada como texto correctamente
if accion == "1" or accion.lower() == "registro":
    haz_El.registro()
elif accion == "2" or accion.lower() == "login":
    haz_El.login()
else:
    haz_El.error()
