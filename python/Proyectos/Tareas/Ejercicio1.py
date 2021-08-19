print("\n Ejercicio 1\n")
n1=int(input("Ingrese un número: "))
n2=int(input("Ingrese otro número: "))
n3=int(input("Ingrese un número más: "))
print("\n")
if n1>n2>n3 or n1>n3>n2:
    oper = n1+n2+n3
    print(f"La suma de: {n1} + {n2} + {n3} = {oper}")
elif n2>n1>n3 or n2>n3>n1:
    oper = n1*n2*n3
    print(f"La multiplicación de: {n1} * {n2} * {n3} = {oper}")    
elif n3>n2>n1 or n3>n1>n2:
    print(f"Los números concatenados son: {n1}{n2}{n3}")
elif n1==n2 and n1!=n3:
    print(f"El número diferente es: {n3}")
elif n1==n3 and n1!=n2:
    print(f"El número diferente es: {n2}")
elif n3==n2 and n3!=n1:
    print(f"El número diferente es: {n1}")    
elif n1==n2==n3:
    print("Los números son iguales")
else:
    print("Opción no vávida")
print("\n__________|Ejercicio finalizado|__________\n")