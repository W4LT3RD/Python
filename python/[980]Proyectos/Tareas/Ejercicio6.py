print("\n Ejercicio 6: \n")

n61 = int(input("Ingrese un número: "))
n62 = int(input("Ingrese otro número: "))

if n61>n62:
    for i in range(n61,n62-1,-1):
        print(i)

elif n62>n61:
    for i in range(n62,n61-1,-1):
        print(i)
else: 
    print("No válido") 