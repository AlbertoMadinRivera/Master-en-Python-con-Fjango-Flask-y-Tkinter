"""
Ejercicio 10.
    El programa tiene que pedir la nota de 15 alumnos
    y sacar por pantalla cuántos han aprobado y cuántos han suspendido.
"""

contador = 1
aprobados = 0
suspendidos = 0

numero_alumnos = int(input("Introduce el número de alumnos que tienes: "))

while contador <= numero_alumnos:
    nota = int(input(f"¿Qué nota quieres ponerle al \"alumno {contador}\"? "))
    if nota >= 6:
        aprobados += 1
    else:
        suspendidos += 1
    contador += 1
print(f"\nAlumnos aprobados: {aprobados}")
print(f"Alumnos suspendidos: {suspendidos}")