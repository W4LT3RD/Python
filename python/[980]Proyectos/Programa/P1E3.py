import psycopg2
print("\n Ingrese fecha de nacimiento\n")
dia=int(input("Día de nacimiento: "))
mes=int(input("Mes de nacimiento: "))
a=int(input("Año de nacimiento: "))
print("\n")
if 2021>a>1900:
    edad=2021-a
    if 12>=mes>=1:
        if mes==1 or mes==3 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
            if 31>=dia>=1:
                if mes<=8 and dia<26:
                    a = "Su edad es "+str(edad)+", usted ya cumplió años"  
                    print(f"Su edad es {edad}, usted ya cumplió años")
                else:
                    a = "Su edad es "+str(edad)+", usted no ha cumplido años"
                    print(f"Su edad es {edad}, usted no ha cumplido años")
            else:
                a="Fecha incorrecta."
                print("Fecha incorrecta")
        elif mes==4 or mes==6 or mes==9 or mes==11:
            if 30>=dia>=1:
                if mes<=8 and dia<26:
                    a = "Su edad es "+str(edad)+", usted ya cumplió años" 
                    print(f"Su edad es {edad}, usted ya cumplió años")
                else:
                    a = "Su edad es "+str(edad)+", usted no ha cumplido años"
                    print(f"Su edad es {edad}, usted no ha cumplido años")
            else:
                a="Fecha incorrecta."
                print("Fecha incorrecta")
        elif mes==2:
            if 28>=dia>=1:
                a = "Su edad es "+str(edad)+", usted ya cumplió años" 
                print(f"Su edad es {edad}, usted ya cumplió años")
            else:
                a="Fecha incorrecta."
                print("Fecha incorrecta")
    print("\n")
else:
    a="Fecha incorrecta."
    print("\nFecha incorrecta\n")

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
        VALUES (""" +str(3)+ """, """+"'"+textoE+"'"+""");""")
print("¡Datos ingresados!\n")
# Cerrar:
conn.commit()
conn.close()
conectar.close()