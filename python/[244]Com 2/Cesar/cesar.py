
L2I = dict(zip("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ",range(26)))
I2L = dict(zip(range(26),"ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"))
key = 3 # corrimiento de bits


np=int(input("""
*Cifrado Cesar*

Opciones a realizar:
1. Cifrar texto.
2. Descifrar código. 
3. Salir del programa.

Ingrese la opción a elegir: """))

if np==2:
    text=input("\nIngrese texto a descifrar: ").upper()
    # desencriptar
    plaintext2=text
    plaintext2 = ""
    for c in text.upper():
        if c.isalpha(): plaintext2 += I2L[ (L2I[c] - key)%26 ]
        else: plaintext2 += c
    print (f"Texto Descifrado: {plaintext2}")
            
elif np==1:
    text=input("\nIngrese el texto a cifrar: ").upper()
    plaintext=text
    ciphertext = ""
    for c in plaintext.upper():
        if c.isalpha(): ciphertext += I2L[ (L2I[c] + key)%26 ]
        else: ciphertext += c
    print (f"Texto Cifrado: {ciphertext}")

        
else:
    print("Opción incorrecta.")
    