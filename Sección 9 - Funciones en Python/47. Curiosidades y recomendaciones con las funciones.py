def mi_funcion(nombre):
    print("Hola, que tal" + nombre)

def mi_segunda_funcion(apellidos):
    return "Hola, que tal " + apellidos


nombre = "Alberto"
apellidos = "Madin Rivera"

print("Hola Mundo")
print(f"Bienvenido, {nombre}")

print(mi_funcion(nombre))
print(mi_segunda_funcion(apellidos))

"""
Lo mejor es llevar órden dentro de un archivo donde se tiene que programar.
Si se tiene que crear varias funciones, siempre hay que crear una función donde se lleve ese orden y poco a poco llevar
la segunda función abajo de la primera.

Lo recomendable siempre es que cuando se define una función, se tiene que crear un return, en vez del print, como se ve
en la primera función.

Siempre es recomendable definir una función global antes de asignarla, porque por ejemplo, si se ponen las funciones
después del print, saldrá un error.
"""