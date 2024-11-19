"""
Ejercicio 3.
    Escribe un programa que muestre los cuadrador
    (un número multiplicado por si mismo) de los 60 primeros números
    nayutales.
        - Resuelvelo con el bucle for y while
"""

# While

contador = 0

while contador <= 60:
    cuadrado = contador * contador
    print(f"El cuadrado de {contador} es {cuadrado}")
    contador += 1
else:
    print("Finalizado")
    print("")
    
    

# For
for  numero in range(61):
    cuadrado = numero * numero
    print(f"Ek cuadrado de {numero} es {cuadrado}")