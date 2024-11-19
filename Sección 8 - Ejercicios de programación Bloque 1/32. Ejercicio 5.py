"""
Ejercicio 5.
    Has un programa que muestre todos los números
    entre dos números que diga el usuario.
"""

numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

# Comprobar que el número 1 sea menor a número 2

if numero1 <  numero2:
    for contador in range(numero1, (numero2 + 1)):
        print(contador)
else:
    print("El número 1 debe de ser menor al número 2")