"""
Podemos crear unas funciones dentro de otras funciones
sin tener ningún problema
"""

def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def getApellidos(apellidos):
    texto = f"Los apellidos son: {apellidos}"
    return texto 

print(getNombre("Alberto"), getApellidos("Madin Rivera"))


# Qué pasaría si quiero usar esa funciones dentro de otra función
def getDevuelveTodo(nombre, apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
    return texto

print("\n")

print(getDevuelveTodo("Alberto", "Madin Rivera"))