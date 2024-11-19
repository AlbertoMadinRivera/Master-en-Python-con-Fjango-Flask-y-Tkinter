"""
Ejercicio 7. 
    Hacer un programa que muestre todos los números impares entre dos números
    que elija el usuario.
"""

numero1 = int(input("Introduce un número: "))
numero2 = int(input("Introduce el segundo número: "))

if numero1 < numero2:
    for x in range(numero1, (numero2 + 1)):
        if x%2 == 0:
            print(f"{x} es par!!")
        else:
            print(f"{x} es impar!!")
else:
    print(f"El número {numero1} debe de ser menor al número {numero2}")