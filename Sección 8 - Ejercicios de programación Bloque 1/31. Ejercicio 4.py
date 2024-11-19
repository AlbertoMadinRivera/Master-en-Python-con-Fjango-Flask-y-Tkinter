"""
Ejercicio 4.
    Pedir dos números al usuario y hacer todas las
    operaciones básicas de una calculadora y mostrarlo por pantalla.
"""

numero1 = int(input("Introduce el primer Número: "))
numero2 = int(input("Introduce el segundo Número: "))

print("####### CALCULADORA ######")
print("Suma: " + str(numero1 + numero2))
print("Resta: " + str(numero1 - numero2))
print("Multiplicación: " + str(numero1 * numero2))
print("División: " + str(numero1 / numero2))