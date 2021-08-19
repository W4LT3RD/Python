print("\n *Ejercicio 2:\n")
nEjer2=int(input("Ingrese un número para mostrar sus divisores: "))
def divisores(nEjer2):
    div=[]
    for i in range(1, nEjer2+1):
        if nEjer2%i==0:
            div.append(i)
    return div
n2Ejer2=divisores(nEjer2)
print(f"Los divisores del número ingresado son: {n2Ejer2}")
