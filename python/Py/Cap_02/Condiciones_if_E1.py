"""
Ejer1: programa debe de decir cuando existe un numero par.
Ejer2: Programa que diga cuál es mayor de 3 números ingresados.
Ejer3: Indicar cuales son vocales
Ejer4: Operaciones aritméticas con dos números.
Ejer5: Cajero automatico con opciones de crédito y débito de dinero, 
    opciones del menú: acreditar, debitar, mostrar dinero, salir.
"""
print("_______________________________________________________________")
print("")
print("Ejercicios posibles para realizar")
print("1. Ingresar dos números para indicar cuales son pares.")
print("2. Ingresar tres números para indicar cuál es mayor.")
print("3. Pedir un caracter e indicar si es vocal o no.")
print("4. Una operación aritmética entre dos números.")
print("5. Cajero automático.")
print("________________________________________________________________")
print("")
np=int(input("Eliga el número de ejercicio que desee empezar: "))
print("________________________________________________________________")
if 5>=np>0:
    print("")
    if np==1:
        print(" *¿Números pares o impares?")
        n1=int(input("Ingrese un número: "))
        n2=int(input("Ingrese otro número: "))

        if n1%2==0 and n2%2==0:
            print("Ambos números son pares")
        elif n1%2==0 and n2%2!=0:
            print(f"Somamente el número {n1} es par.")
        elif n1%2!=0 and n2%2==0:
            print(f"Solamente el número {n2} es par.")
        else:
            print("Los números son impares")  

    if np==2:
        print(" *Número mayor:")
        print("")
        m1=int(input("Ingrese primer número: "))
        m2=int(input("Ingrese primer número: "))
        m3=int(input("Ingrese primer número: "))
        print("")
        if m1>m2>m3 or m1>m3>m2:
            print(f"El número {m1} es el mayor.")
        if m2>m1>m3 or m2>m3>m1:
            print(f"El número {m2} es el mayor.")
        if m3>m2>m1 or m3>m1>m2:
            print(f"El número {m3} es el mayor.")
    
    if np==3:
        print(" * ¿Vocal o no?:")
        print("")
        l1=input("Ingrese un caracter: ").lower() # .lower() hace que la letra que se ingrese se pase a minúscula
        # l1 = l1.lower() hace el mismo proceso de arriba
        # l1 = l1.upper 
        print("")
        if l1=='a' or l1=='e' or l1=='i' or l1=='o' or l1=='u':
            print("El caracter ingresado es una vocal")
        else:
            print("El caracter ingresado es una consonante")
    
    if np==4:
        print(" * Operación aritemética:")
        print("")
        n14=float(input("Ingrese el primer número: "))
        n24=float(input("Ingrese el segundo número: "))
        print("\n¿Qué operación le gustaría hacer?")
        print("S. Suma.")
        print("R. Resta.")
        print("M. Multiplicación.")
        print("D. División.")
        loper=input("\nIngrese la letra: ").upper()
        if loper=='S':
            oper=n14+n24
            print(f"\nLa suma de: {n14} + {n24} = {oper}")
        elif loper=='R':
            oper=n14-n24
            print(f"\nLa resta de: {n14} - {n24} = {oper}")
        elif loper=='M' or loper=='P':
            oper=n14*n24
            print(f"\nLa multiplicación de: {n14} * {n24} = {oper}")
        elif loper=='D':
            oper=n14/n24
            print(f"\nLa división de: {n14} / {n24} = {oper}")
        else:
            print(f"\nLa letra {loper} no es válida")
    
    if np==5:
        din=1000
        opcion=int(input("""
        Bienvenido a tu cajero automático

        Por favor elegir una opción:
        1. Acreditar dinero.
        2. Debitar dinero.
        3. Mostrar dinero actual
        4. Salir

        Opcion a realizar: """))
        print()
        if opcion==1:
            credit=float(input("Ingrese el saldo a acreditar: Q"))
            din+=credit
            print(f"Dinero total en su cuenta es: Q{din}")
        elif opcion==2:
            debit=float(input("Ingrese el saldo a debitar: Q"))
            if debit>din:
                print("No posee el dinero suficiente.")
            else:
                din-=debit
                print(f"El dinero total en su cuenta es: Q{din}")
        elif opcion==3:
            print(f"Su saldo actual es: Q{din}")
        elif opcion==4:
            print("Gracias por usar nuestro servicio. Vuelva pronto.")
        else:
            print("Opción incorrecta.")




else:
    print(f'\nEl número {np} es inválido.')

print("________________________________________________________________")
print("\n______________________|Programa finalizado|_____________________\n")