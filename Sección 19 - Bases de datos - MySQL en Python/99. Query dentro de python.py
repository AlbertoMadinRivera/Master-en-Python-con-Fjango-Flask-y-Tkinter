import mysql.connector

# Conexión a la base de datos
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",  # Contraseña de MySQL
        database="master_python"
    )

# Consultar todos los estudiantes
def get_estudiantes():
    db_connection = get_connection()
    cursor = db_connection.cursor(dictionary=True)  # Usamos dictionary para obtener resultados más legibles

    cursor.execute("SELECT * FROM estudiantes")
    estudiantes = cursor.fetchall()

    cursor.close()
    db_connection.close()

    return estudiantes

# Consultar todos los cursos
def get_cursos():
    db_connection = get_connection()
    cursor = db_connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM cursos")
    cursos = cursor.fetchall()

    cursor.close()
    db_connection.close()

    return cursos

# Consultar matriculas de un estudiante
def get_matriculas_por_estudiante(estudiante_id):
    db_connection = get_connection()
    cursor = db_connection.cursor(dictionary=True)

    query = """
    SELECT estudiantes.nombre AS estudiante, cursos.nombre_curso, matriculas.fecha_matricula
    FROM matriculas
    JOIN estudiantes ON matriculas.id_estudiante = estudiantes.id
    JOIN cursos ON matriculas.id_curso = cursos.id
    WHERE estudiantes.id = %s
    """
    cursor.execute(query, (estudiante_id,))
    matriculas = cursor.fetchall()

    cursor.close()
    db_connection.close()

    return matriculas

# Ejemplo de uso
if __name__ == "__main__":
    # Obtener estudiantes
    estudiantes = get_estudiantes()
    print("Estudiantes:")
    for estudiante in estudiantes:
        print(f"ID: {estudiante['id']}, Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}, Email: {estudiante['email']}")

    # Obtener cursos
    cursos = get_cursos()
    print("\nCursos:")
    for curso in cursos:
        print(f"ID: {curso['id']}, Nombre del Curso: {curso['nombre_curso']}, Descripción: {curso['descripcion']}")

    # Consultar matriculas de un estudiante (por ejemplo, ID 1)
    matriculas = get_matriculas_por_estudiante(1)
    print("\nMatriculas del Estudiante 1:")
    for matricula in matriculas:
        print(f"Curso: {matricula['nombre_curso']}, Fecha de Matrícula: {matricula['fecha_matricula']}")
