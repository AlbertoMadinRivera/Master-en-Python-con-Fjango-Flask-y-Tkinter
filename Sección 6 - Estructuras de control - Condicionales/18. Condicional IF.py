# Un condicional es una estructura de control siempre y cuando
# se cumpla esa instrucción de la condición, dependiendo de la entrada de dato
# que ponga el usuario

""""
# Condicional IF

SI se_cumple_esta_condición:
    Ejecuta el grupo de instrucciones
SI NO:
    Se ejecutan otro grupo de instrucciones

# Ejemplo más detallado Python

if confición:
    instrucciones
else:
    otras condiciones
"""

# Ejemplo 1
print("")
print("########## Ejemplo 1 ##########")
print("")

color = "Rojo"

if color == "Rojo":
    print("¡FELICIDADES!")
    print("El color es ROJO")
else:
    print("El color NO es ROJO")

# Ejemplo 2
print("")
print("########## Ejemplo 2 ##########")
print("")

color = input("Adivina mi color favorito...")


if color == "Rojo":
    print("¡FELICIDADES!")
    print("El color es ROJO")
else:
    print("El color NO es ROJO")