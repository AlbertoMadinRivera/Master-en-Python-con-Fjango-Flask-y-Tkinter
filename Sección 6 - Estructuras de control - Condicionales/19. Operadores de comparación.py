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

## Ejemplo 1
#print("")
#print("########## Ejemplo 1 ##########")
#print("")
#
#color = "Rojo"
#
#if color == "Rojo":
#    print("¡FELICIDADES!")
#    print("El color es ROJO")
#else:
#    print("El color NO es ROJO")
#
## Ejemplo 2
#print("")
#print("########## Ejemplo 2 ##########")
#print("")
#
#color = input("Adivina mi color favorito...")
#
#
#if color == "Rojo":
#    print("¡FELICIDADES!")
#    print("El color es ROJO")
#else:
#    print("El color NO es ROJO")

""""
# Operadores de comparación

== igual
!= diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que
"""

# Ejemplo 3
print("")
print("########## Ejemplo 3 ##########")
print("")

year = 2020

if year >= 2021:
    print("Estamos de 2021 en adelante!!")
else:
    print("Es un año anterior a 2021...")


# Ejemplo 4
print("")
print("########## Ejemplo 4 ##########")
print("")

year = int(input("¿En qué año estamos? "))

if year >= 2021:
    print("Estamos de 2021 en adelante!!")
else:
    print("Es un año anterior a 2021...")


# Ejemplo 5
print("")
print("########## Ejemplo 5 ##########")
print("")

year = int(input("¿En qué año estamos? "))

if year != 2021:
    print("El año es diferente de 2021")
else:
    print("Estamos en 2021!!!")