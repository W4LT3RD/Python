import psycopg2

print("Verificar si un número es primo:")
e11=int(input("\nIngrese un número: "))

if e11>1:
    cont = 0
    for i in range(2, e11):
        residuo = e11 % i
        if residuo == 0:
            cont+=1
    if cont == 0:
        a="El número "+str(e11)+" es primo" 
        print(f"\nEl número {e11}, es primo")
    else:
        a="El número "+str(e11)+", es compuesto" 
        print(f"\nEl número {e11}, es compuesto\n")
else:
    a="El número es incorrecto" 
    print("\nNúmero incorrecto")

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
        VALUES (""" +str(1)+ """, """+"'"+textoE+"'"+""");""")
print("¡Datos ingresados!\n")
# Cerrar:
conn.commit()
conn.close()
conectar.close()