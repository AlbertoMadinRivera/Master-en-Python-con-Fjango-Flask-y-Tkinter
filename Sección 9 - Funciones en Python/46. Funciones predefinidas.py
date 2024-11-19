"""
Funciones predefinidas dentro de python
"""

# Funciones generales
nombre = "Alberto Madin Rivera"

print(type(nombre))


# Detectar el tipado
comprobar = isinstance(nombre, str) # int

if comprobar:
    print("Esa variable es un string")
else:
    print("No es una cadena")

if not isinstance(nombre, float):
    print("La variable no es un número con decimales")


# Limpiar espacios de un string
frase = "    mi contenido          "

print(frase)
print(frase.strip()) # Limpia todos los espacios que tiene a lado


# Eliminar variables
year = 2024
print(year)
del year 
#print(year) # No existe


# Comprobar variables vacías
texto = "     ffff       "
if len(texto) <= 0:
    print("La variabler está vacía")
else:
    print("La variable tiene contenido:", len(texto))


# Encontrar carácteres
frase = "La vida es bella"
print(frase.find("vida")) # Está en el carácter 3


# Reemplazar palabras en un string
nueva_frase = frase.replace("vida", "moto")
print(nueva_frase)


# Procesar mayúsculas y minúsculas
print(nombre)
print(nombre.lower())
print(nombre.upper())