"""
Una variable local es una que se define dentro de la función y no puede ser usada fuera de la función.
Una variable global son las que se usan dentro y fuera de una función.
"""

# Variable global
frase = "Ni los gemelos se conocen tanto"

print(frase)

def holaMundo():
    frase = "Hola Mundo!" # Al momento de que se comente esta 'frase' se vuelve global
    print("Dentro de la función:")
    print(frase)

    year = 2024
    print(year)

holaMundo()
# print(year) # Variable local

print("\n")

def holaMundo():
    frase = "Hola Mundo!" # Al momento de que se comente esta 'frase' se vuelve global
    print("Dentro de la función:")
    print(frase)

    year = 2024
    print(year)

    global website # De esta forma la variable website es global y local de la función
    website = "albertomadin.com"
    print("DENTRO: ", website)

    return "Dato devuelto " + str(year)

print(holaMundo())
print("FUERA: ", website)

