import psycopg2
print("\nCrear tabla de multiplicar del número ingresado\n")

n41=int(input("Ingrese un número: "))
print("")
for i in range(1, 11):
    result = i*n41
    a=str(n41)+"x"+str(i)+"="+str(result)
    print(f"{n41} x {i} = {result}")
print("\n")

textoE = a
try: # try se utiliza con except, normalmente muestra la conexión exitosa o fallida con la base de datos
    # Creando conexión:
    conn = psycopg2.connect(host = 'localhost', database = 'postgres', user = 'postgres', password = 135792468)
    print("\n¡Conexión exitosa!\n")
except: 
    print("Error en la conexión...")
# Creando cursor: para interactuar con DB: 
conectar = conn.cursor()
# Ingresar datos:
conectar.execute("""
    INSERT INTO public."Ejercicios"(
        "Ejercicio", "Respuesta") 
        VALUES (""" +str(4)+ """, """+"'"+textoE+"'"+""");""")
print("Datos ingresados!\n")
# Cerrar:
conn.commit()
conn.close()
conectar.close()