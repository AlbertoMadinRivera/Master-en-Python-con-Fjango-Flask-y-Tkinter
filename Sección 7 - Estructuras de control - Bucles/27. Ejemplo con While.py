# Ejemplo while

print("### Ejemplo ###")

numero_usuario = int(input("¿De qué número quieres la tabla?:"))

if numero_usuario < 1:
    numero_usuario = 1

print(f"### Tabla del {numero_usuario} ###")

contador = 1
while contador <= 10:
    print(f"{numero_usuario} X {contador} = {numero_usuario*contador}")
    contador += 1
else:
    print("\nTabla terminada")