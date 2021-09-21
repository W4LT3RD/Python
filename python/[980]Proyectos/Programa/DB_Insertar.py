import psycopg2
num=1
texto = "Texto de ejercicio 1"
ejercicio = num
textoE = texto
try: # try se utiliza con except, normalmente muestra la conexión exitosa o fallida con la base de datos
    # Creando conexión:
    conn = psycopg2.connect(host = 'localhost', database = 'postgres', user = 'postgres', password = 135792468)
    print("\n¡Conexión exitosa!\n")
except: 
    print("Error en la conexión...")
# Creando cursor: para interactuar con DB: 
conectar = conn.cursor()
# Ingresar datos:
conectar.execute("""INSERT INTO public."Ejercicios"("Ejercicio", "Respuesta") VALUES (""" + str(ejercicio) + """, """+"'"+textoE+"'"+""");""")
print("Datos ingresados!")
# Cerrar:
conn.commit()
conn.close()
conectar.close()