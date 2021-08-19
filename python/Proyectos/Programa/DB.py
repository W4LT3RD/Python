import psycopg2
# Creando conexión:
conn = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    user = 'postgres', 
    password = 135792468
    )
print("Conexión exitosa\n")

# Creando cursor: para interactuar con DB:
cursor = conn.cursor()

# Para mandar datos a DB:
cursor.execute("DROP TABLE IF EXISTS ALUMNOS") #Para que no se cree otra tabla con el mismo nombre 
SQL = """
    CREATE TABLE Alumnos(
        Nombre CHAR(20) NOT NULL,
        Apellido CHAR (20) NOT NULL,
        Edad INT,
        Calificación FLOAT
    )"""
cursor.execute(SQL)
print("\nTabla creada con éxito  \n")

conn.commit() # Para guardar cambios.

# Cerrar:
conn.close()