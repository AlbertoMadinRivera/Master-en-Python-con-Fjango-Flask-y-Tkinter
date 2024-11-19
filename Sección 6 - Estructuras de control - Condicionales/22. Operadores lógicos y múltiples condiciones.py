# Un condicional es una estructura de control siempre y cuando
# se cumpla esa instrucción de la condición, dependiendo de la entrada de dato
# que ponga el usuario

#""""
## Condicional IF
#
#SI se_cumple_esta_condición:
#    Ejecuta el grupo de instrucciones
#SI NO:
#    Se ejecutan otro grupo de instrucciones
#
## Ejemplo más detallado Python
#
#if confición:
#    instrucciones
#else:
#    otras condiciones
#"""

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

#""""
## Operadores de comparación
#
#== igual
#!= diferente
#< menor que
#> mayor que
#<= menor o igual que
#>= mayor o igual que
#"""
#
## Ejemplo 3
#print("")
#print("########## Ejemplo 3 ##########")
#print("")
#
#year = 2020
#
#if year >= 2021:
#    print("Estamos de 2021 en adelante!!")
#else:
#    print("Es un año anterior a 2021...")
#
#
## Ejemplo 4
#print("")
#print("########## Ejemplo 4 ##########")
#print("")
#
#year = int(input("¿En qué año estamos? "))
#
#if year >= 2021:
#    print("Estamos de 2021 en adelante!!")
#else:
#    print("Es un año anterior a 2021...")
#
#
## Ejemplo 5
#print("")
#print("########## Ejemplo 5 ##########")
#print("")
#
#year = int(input("¿En qué año estamos? "))
#
#if year != 2021:
#    print("El año es diferente de 2021")
#else:
#    print("Estamos en 2021!!!")

## Ejemplo 6
#print("")
#print("########## Ejemplo 6 ##########")
#print("")
#
#nombre = "Alberto Madin Rivera"
#ciudad = "Ciudad de México"
#continente = "America"
#edad = 27
#mayoria_edad = 18
#
#if edad >= mayoria_edad:
#    # Instrucciones
#    print(f"La persona: {nombre} SI es es mayor de edad")
#
#    if continente != "America":
#        print("El usuario NO es Americano")
#    else:
#        print(f"El usuario: {nombre} es Americano y de la {ciudad}")
#else:
#    print(f"La persona: {nombre}, NO es mayor de edad")

## Ejemplo 7
#print("")
#print("########## Ejemplo 7 ##########")
#print("")
#
#dia = int(input("Introduce el día de la semana: "))
#
#if dia == 1:
#    print("Es Lunes!!")
#else:
#    if dia == 2:
#        print("Es martes!!")
#    else:
#        if dia == 3:
#            print("Es miércoles!!")
#        else:
#            if dia == 4:
#                print("Es jueves!!")
#            else:
#                if dia == 5:
#                    print("Es viernes")
#                else:
#                    print("Es fin de semana!!!")
#
#"""
#ELIF ayuda a llevar un mejor control. Llevando a seguir un control de condiciones
#"""
#
## Ejemplo 8
#print("")
#print("########## Ejemplo 8 ##########")
#print("")
#
#dia = int(input("Introduce el día de la semana: "))
#
#if dia == 1:
#    print("Es lunes")
#elif dia == 2:
#    print("Es martes")
#elif dia == 3:
#    print("Es miércoles")
#elif dia == 4:
#    print("Es jueves")
#elif dia == 5:
#    print("Es viernes")
#else:
#    print("Es fin de semana")

# Ejemplo 9
print("")
print("########## Ejemplo 9 ##########")
print("")

edad_minima = 18
edad_maxima = 60
edad_oficial = int(input("¿Tienes edad de trabajar? "))

if edad_oficial >= 18 and edad_oficial <= 60:
    print("Está en edad de trabajar!!")
else:
    print("No está en edad de trabajar")

"""
# Operadores lógicos
and:    Y
or:     O
!:      Negación
not:    NO
"""