# Ejemplo 4
print("########## Ejemplo 4 ##########")

"""
Parámetros opcionales
"""

print("\n")

def getEmpleado(nombre, ID):
    print("EMPLEADO")
    print(f"Nombre: {nombre}")
    print(f"ID: {ID}")

getEmpleado("Alberto Madin Rivera", "2163019389")

print("\n")

# Queremos que el ID sea un parámetro opcional
# Le ponemos como parámetro a la función que queremos que ID sea un Booleano Falso (False)
# Y le ponemos una condición para que se muestre o no se muestre !=

def getEmpleado(nombre, ID = False):
    print("EMPLEADO")
    print(f"Nombre: {nombre}")

    if ID != False:
        print(f"ID: {ID}")

getEmpleado("Alberto Madin Rivera")
getEmpleado("Akberto Madin Rivera", 12345)