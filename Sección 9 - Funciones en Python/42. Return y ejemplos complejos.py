# Ejemplo 5: Parámetros opcionales y return para devolver datos
print("########## EJEMPLO 5 ##########")

print("\n")

def Saludame(nombre):
    saludo = f"Hola, Saludos {nombre}!!!"

    return saludo

# No aparece nada
Saludame("Alberto")

# Debemos de darle un print
print(Saludame("Alberto Madin Rivera"))


print("\n")

print("########## Ejemplo 6 ##########")

print("\n")

def Calculadora(numero1, numero2, basicas = False):
    suma = numero1 + numero2
    resta = numero1 - numero2 
    multi = numero1 * numero2 
    division = numero1 / numero2 

    cadena = ""

    cadena += "La Suma es: " + str(suma)
    cadena += "\n"
    cadena += "La Resta es: " + str(resta)
    cadena += "\n"
    cadena += "La Multiplicación es: " + str(multi)
    cadena += "\n"
    cadena += "La División es: " + str(division)

    return cadena

print(Calculadora(4, 9))

"""
Ahora, queremos que nos saque las operaciones básicas que se le hizo a la 
función, así que se va a hacer eso desde la función anterior con un 'if'
"""

print("\n")
print("Segundo caso")
print("\n")

def Calculadora(numero1, numero2, basicas = False):
    suma = numero1 + numero2
    resta = numero1 - numero2 
    multi = numero1 * numero2 
    division = numero1 / numero2 

    cadena = ""

    if basicas != False:

        cadena += "La Suma es: " + str(suma)
        cadena += "\n"
        cadena += "La Resta es: " + str(resta)
        cadena += "\n"

    else:

        cadena += "La Multiplicación es: " + str(multi)
        cadena += "\n"
        cadena += "La División es: " + str(division)

    return cadena

print(Calculadora(10, 5, basicas = True)) # Obtenemos las operaciones básicas
print(Calculadora(10, 5, basicas = False)) # Obtenemos las operaciones no básicas