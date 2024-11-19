"""
Ejercicio 8.
    ¿Cuánto es el X por ciento de X número?
    ¿Cuánto es el 20 por ciento de 150?
"""

numero = int(input("Introduce el número a analizar: "))
porcentaje = int(input(f"¿Qué porcentaje quieres sacar de {numero}? "))

operacion = (numero * (porcentaje/100))

print(f"El {porcentaje}% de {numero} es: {operacion}")