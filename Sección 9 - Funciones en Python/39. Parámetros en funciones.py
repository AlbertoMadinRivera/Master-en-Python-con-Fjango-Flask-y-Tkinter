# Ejemplo 2: parámetros
print("######### EJEPLO 2 #########")

nombre = input("Define tu nombre: ")
edad = int(input("¿Qué edad tienes? "))

def mostrar_tu_nombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")
    if edad >= 18:
        print("Y eres mayor de edad c:")
    else:
        print("Y no eres mayor de edad :c")

mostrar_tu_nombre(nombre, edad)
