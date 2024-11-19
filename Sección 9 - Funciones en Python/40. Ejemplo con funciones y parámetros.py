## Ejemplo 2: parámetros
#print("######### EJEPLO 2 #########")
#
#nombre = input("Define tu nombre: ")
#edad = int(input("¿Qué edad tienes? "))
#
#def mostrar_tu_nombrse(nombre, edad):
#    print(f"Tu nombre es: {nombre}")
#    if edad >= 18:
#        print("Y eres mayor de edad c:")
#    else:
#        print("Y no eres mayor de edad :c")
#
#mostrar_tu_nombre(nombre, edad)

# Ejemplo 3
print("########## Ejemplo 3 ##########")
print("\n")

def tabla(numero):
    print(f"Tabla de multiplicar del número: {numero}")
    
    for contador in range(11):
        operacion = numero*contador
        print(f"{numero} x {contador} = {operacion}")
    
    print("\n")
    
tabla(4)
tabla(8)


print("\n")
print("---------------------------------")

for numeto_tabla in range(1,11):
    tabla(numeto_tabla)