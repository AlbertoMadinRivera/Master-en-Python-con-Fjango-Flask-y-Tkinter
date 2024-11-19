class Acciones:
    
    def registro(self):
        print("De acuerdo, vamos a registrarte en el sistema...")
        
        nombre = input("¿Cuál es tu nombre? ")
        apellidos = input("¿Cuáles son tus apellidos? ")
        email = input("Introduce un email: ")
        password = input("Introduce tu contraseña: ")
    
    def login(self):
        print("De acuerdo, es necesario que te identifiques dentro del sistema...")
        email = input("Introduce un email: ")
        password = input("Introduce tu contraseña: ")

    def error(self):
        print("Opción no válida. Por favor, elige 1 para Registro o 2 para Login.")