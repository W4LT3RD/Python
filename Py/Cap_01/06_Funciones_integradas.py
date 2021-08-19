# Funciones integradas de py
"""
    Se utilizan para hacer conversiones de datos
"""
print("\n__________________________'FUNCIONES INTEGRADAS DE PY'_______________________________")
m=-245.8
print("\nm = -245.8")
print(f"Obteniendo el valor absoluto con: abs(m) = {abs(m)}")
print(f"\nRedondeando valor al más próximo con: round(m) = {round(m)}")
n='Walter' 
print("\nSi se tiene un texto: n='Walter'")
print(f"Para calcular la canitad de letras se utiliza: len(n) = {len(n)}")


print("\n * Conversion de números:\n")
a=int("10") # Aqui se convierte el "texto" que es un 10 a un valor entero 10
print(a)
b=float("50") # Convertimos el texto 50 a un valor flotante 50.0
b+=10
print(b+10)
# Proceso inverso: convirtiendo de números a texto o cadena, se utiliza <str>, 
# RECODAR QUE CON UN TEXTO NO SE PUEDEN HACER OPERACIONES MATEMATICAS

c=str(10.25)
# c+=10 <- esto es incorrecto ya que le estamos sumando un número a un texto.
print(f"Texto: {c}")

# Para convertir un número a binario o hexadecimal.
d=75
print("\nTeniendo: d=75")
print(f"Convirtiendo a binario, con bin(d) = {bin(d)}") # El resultado será: 0b1001011, 0b significa que es un valor binario. 
print(f"Convirtiendo a hexadecimal, con hex(d) = {hex(d)}\n") # El resultado será: 0x4b, 0x significa que es un valor hexadecimal.

#Convirtiendo valor hexadecimal o binario a un decimal (base diez)
e='0x16' # Los valores hexadecimales o binarios, Py los toma como cadenas o texto.
print("Teniendo: e='0x16'")
# Se debe de escribir tipo de dato se desea convertir, seguido de la base
print(f"Se puede convertir a decimal como: int(e, 16) = {int(e, 16)}") 


f='0b1101'
print("\nAhora teniendo f='0b1101'")
print(f"Se puede convetir a decimal como: int(f,2) = {int(f, 2)}\n")

