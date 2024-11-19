# Ejemplo con tablas de multiplicar
print("\n ########## Ejemplo ##########")

numero_usuario = int(input("¿De qué número quieres ver la tabla? "))

if numero_usuario < 1:
    numero_usuario = 1

print(f"\n ### Tabla e multiplicar del número {numero_usuario} ###")

for numero_tabla in range(1, 11):
    if numero_usuario == 45:
        print("No se pueden mostrar números prohibidos!!")
        break # Rompe el bucle
    print(f"{numero_usuario} X {numero_tabla} = {numero_usuario*numero_tabla}")
else:
    print("Tabla finalizada.")