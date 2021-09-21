import base64

text=input("""
\t#Codificación propia
Por favor ingrese el texto: """)
opc=int(input("""
¿Qué desea hacer con el texto ingresado?
1. Codificar.
2. Decodificar.

Ingrese la opción: """))

# Codificación en Base64:
codificacion = base64.b64encode(text)
print(f"Texto codificado: {codificacion}")

# Decodificación en Base64:
print(f"Texto decodificado: {base64.b64decode(codificacion)}")