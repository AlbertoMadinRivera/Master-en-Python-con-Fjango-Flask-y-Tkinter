# Un bucle es una estructura donde se repite varias veces una codición.
"""
# FOR
for variable in elemento_iterable (lista, rango, etc, tupla, etc.)
    BLOQUE DE INSTRUCCIONES
"""

contador = 0
resultado = 0

for contador in range(0, 15):
    print("Voy por el número: " + str(contador))
    resultado = resultado + contador

print(f"El resultado del bucle es {resultado}")