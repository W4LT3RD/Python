import psycopg2
print("Cantidad de unidades decenas y centenas de un número:\n")
n31=int(input("Ingrese un número entre 1 y 999: "))
if 999>=n31>=1:
    uni = n31 // 1 % 10
    des = n31 // 10 % 10
    cent = n31 // 100 % 10
    print(f"\nUnidades: {uni}, decenas: {des}, centenas: {cent} \n")
    a="Unidades: "+str(uni)+", decenas: "+str(des)+", centenas"+str(cent)

else: 
    print("El número es incorrecto.")
    a="El número es incorrecto"

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
        VALUES (""" +str(2)+ """, """+"'"+textoE+"'"+""");""")
print("¡Datos ingresados!\n")
# Cerrar:
conn.commit()
conn.close()
conectar.close()