print("\n Ejercicio 3: \n")
fraseEj3 = input("Ingrese una palabra para saber cuánta vocales posee: ")

def cont_vocal (fraseEj3):
    vocales="aeiouAEIOU"
    return [elemento for elemento in fraseEj3 if elemento in vocales]

print(f"\nLas vocales son: {cont_vocal(fraseEj3)}")
print(f"\nLa cantidad de vocales es: {len(cont_vocal(fraseEj3))}")
