"""
    Poniendo a prueba los conceptos anteriormente obtenidos:
    Realizando ejericios, como ya se tiene un poco más de práctica se utilizará un 
    if para tener los ejercicios como en un menú a elegir

    Ejercicio 1: Realizar la expresión:
    a^3 * (b^2 - 2 ac)
    ------------------
           2b

    Ejercicio 2: Realizar lo siguiente:
    ((3+5*8)<3 and ((-6*4)+2<2)) or (a>b)
                      --
                      3

    Ejercicio 3: Intercambio de valores
    a=10    -> a=5
    b=5     -> b=10

    Ejercicio 4: Programa que calcule el área y la longitud de una circunferencia.
    área = pi*r^2
    lóngitud = 2*pi*r

    Ejercicio 5: Programa que realice 15% de descuento sobre una compra
"""
import math #Imortando el módulo o biblioteca "math", para utilizar la constante pi
print("\n--------------------Ejercicios de conceptos básicos------------------------\n")
print(" 1. Ejercicio matemático.")
print(" 2. Ejercicio con números y operadores lógicos.")
print(" 3. Ejercicio que intercambia dos variables ingresadas.")
print(" 4. Calcular el área y longitud de una circunferencia.")
print(" 5. Calcular el valor de una compra con el 15% de descuento.")
np=int(input("\nIngresa el número de ejercicio para verificar el funcionamiento: "))
print("\n")
if np==5:
    n51=float(input("Ingresa el total de la compra: Q"))
    des=n51*0.15
    totaldes=n51-des
    print(f"\nEl 15% de descuento es: Q{des:.2f}")
    print(f"El total a pagar es: Q{totaldes:.2f}")

elif np==4:
    n41=float(input("Ingrese el radio de la circunferencia: "))
    n42=input("Magnitud física del radio: ")
    r=n41
    mag=n42
    area= math.pi * r**2
    lon=2*math.pi*r
    print(f"\nÁrea de la circunferencia: {area:.2f} {mag}^2") # La respuesta será 28.274333882308138, por lo que 
    # se utilizó :.2f para que muestre solamente dos decimales, esto pertenece al módulo importado math     
    print(f"Longitud de la circunferencia: {lon:.2f} {mag}")

elif np==3:
    n31=float(input("Ingrese el valor de a: "))
    n32=float(input("Ingrese el valor de b: "))
    n31, n32 = n32, n31 # n31 guardará el valor de n32  y n32 guardará el valor de n31
    a=n31
    b=n32
    print(f"\nValores intercambiados: a = {a}, b = {b}")
elif np==2:
    n21=float(input("Ingrese el valor de a: "))
    n22=float(input("Ingrese el valor de b: "))
    a=n21
    b=n22
    resp1=(3 + 5 * 8) < 3 and (((-6/3)*4) + 2 < 2 ) or (a>b)
    print(f"\n La respuesta de los valores ingresados es: {resp1}")
elif np==1:
    n11=float(input("Ingresa el valor de a: "))
    n12=float(input("Ingresa el valor de b: "))
    n13=float(input("Ingresa el valor de c: "))
    a=n11
    b=n12
    c=n13
    resp1=(a**3 * (b**2 - 2*a*c))/(2*b)
    print(f"\nEl resultado de los números ingresados es: {resp1}")
else: 
    print("\nNúmero incorrecto.")
print("\n------------------------------Fin del programa---------------------------------------\n")