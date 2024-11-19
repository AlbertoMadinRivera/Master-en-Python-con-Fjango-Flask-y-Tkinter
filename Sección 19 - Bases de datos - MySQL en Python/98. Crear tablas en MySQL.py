import mysql.connector
import random
from faker import Faker

# Conexión a la base de datos
database = mysql.connector.connect(
    host="localhost",       # Servidor MySQL local
    user="root",            # Usuario de la base de datos
    passwd="",              # Contraseña (vacía por defecto en XAMPP)
    database="master_python"  # Base de datos a utilizar
)

cursor = database.cursor()

# Crear la tabla 'estudiantes'
cursor.execute("""
CREATE TABLE IF NOT EXISTS estudiantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    edad INT,
    email VARCHAR(255)
)
""")

# Crear la tabla 'cursos'
cursor.execute("""
CREATE TABLE IF NOT EXISTS cursos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_curso VARCHAR(255),
    descripcion TEXT
)
""")

# Crear la tabla 'matriculas' (relaciona estudiantes y cursos)
cursor.execute("""
CREATE TABLE IF NOT EXISTS matriculas (
    id_estudiante INT,
    id_curso INT,
    fecha_matricula DATE,
    FOREIGN KEY (id_estudiante) REFERENCES estudiantes(id),
    FOREIGN KEY (id_curso) REFERENCES cursos(id),
    PRIMARY KEY (id_estudiante, id_curso)
)
""")

# Insertar datos aleatorios en la tabla 'estudiantes' y 'cursos'
fake = Faker()

# Insertar 5 estudiantes aleatorios
for _ in range(5):
    nombre = fake.name()
    edad = random.randint(18, 25)  # Edad aleatoria entre 18 y 25 años
    email = fake.email()
    cursor.execute("INSERT INTO estudiantes (nombre, edad, email) VALUES (%s, %s, %s)", (nombre, edad, email))

# Insertar 3 cursos aleatorios
cursos = [
    ("Matemáticas", "Curso de matemáticas avanzadas."),
    ("Historia", "Estudio de la historia mundial."),
    ("Programación", "Introducción a la programación y desarrollo de software.")
]

for curso in cursos:
    cursor.execute("INSERT INTO cursos (nombre_curso, descripcion) VALUES (%s, %s)", curso)

# Relacionar estudiantes con cursos (matriculaciones aleatorias)
estudiantes_ids = [1, 2, 3, 4, 5]  # IDs de los estudiantes insertados
cursos_ids = [1, 2, 3]            # IDs de los cursos insertados

# Realizar 3 matriculaciones aleatorias
for _ in range(3):
    id_estudiante = random.choice(estudiantes_ids)
    id_curso = random.choice(cursos_ids)
    fecha_matricula = fake.date_this_decade()  # Fecha aleatoria dentro de esta década
    cursor.execute("INSERT INTO matriculas (id_estudiante, id_curso, fecha_matricula) VALUES (%s, %s, %s)", (id_estudiante, id_curso, fecha_matricula))

# Confirmar los cambios
database.commit()

# Consultar los datos insertados
cursor.execute("SELECT * FROM estudiantes")
estudiantes = cursor.fetchall()
print("Estudiantes:")
for estudiante in estudiantes:
    print(estudiante)

cursor.execute("SELECT * FROM cursos")
cursos = cursor.fetchall()
print("\nCursos:")
for curso in cursos:
    print(curso)

cursor.execute("SELECT * FROM matriculas")
matriculas = cursor.fetchall()
print("\nMatriculas:")
for matricula in matriculas:
    print(matricula)

# Cerrar la conexión
cursor.close()
database.close()
