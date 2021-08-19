print("\n *Ejercicio 5: \n")
print("Mostrar números de dos en dos, del número inicial, al número final: \n")
n51 = int(input("Ingrese numero inicial: "))
n52 = int(input("Ingrese numero final: "))

print(f"El conteo desde {n51} hasta {n52} en dos en dos es: ")
for i in range(n51,n52+1,2):
	print(i)