import psycopg2
# Creando conexión:
try: # try se utiliza con except, normalmente muestra la conexión exitosa o fallida con la base de datos
    conn = psycopg2.connect(host = 'localhost', database = 'postgres', user = 'postgres', password = 135792468)
    print("\n¡Conexión exitosa!\n")
    # Creando cursor: para interactuar con DB: 
    mostrar = conn.cursor()
    # Para ver datos a DB:
    Ver_datos="""
        SELECT * FROM redes;
    """
    mostrar.execute(Ver_datos)
    # fetchall, todos los datos:
    datos = mostrar.fetchall()
    # mostrar los datos:
    print(datos)
except: 
    print("Error en la conexión...")
# Cerrar:
conn.close()