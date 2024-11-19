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

print("""
Acciones disponibles:
      1. Registro
      2. Login
""")

accion = input("¿Qué deseas realizar? (Escribe el número o la opción): ")

# Asegúrate de manejar la entrada como texto correctamente
if accion == "1" or accion.lower() == "registro":
    print("De acuerdo, vamos a registrarte en el sistema...")
    nombre = input("¿Cuál es tu nombre? ")
    apellidos = input("¿Cuáles son tus apellidos? ")
    email = input("Introduce un email: ")
    password = input("Introduce tu contraseña: ")

elif accion == "2" or accion.lower() == "login":
    print("De acuerdo, es necesario que te identifiques dentro del sistema...")
    email = input("Introduce un email: ")
    password = input("Introduce tu contraseña: ")

else:
    print("Opción no válida. Por favor, elige 1 para Registro o 2 para Login.")