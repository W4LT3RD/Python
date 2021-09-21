"""
Cifrado Hill
Notación importante:
K = Matriz llave
P = Vector del texto (en números)
C = Vector de texto cifrado (en números)
C = E (K, P) = K * P (módulo X) - X es la longitud del alfabeto utilizado
P = D (K, C) = inv (K) * C (módulo X) - X es la longitud del alfabeto utilizado
"""
import numpy as np
from egcd import egcd # pip install librerías

alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

letter_to_index = dict(zip(alphabet, range(len(alphabet)))) # Establece el rango de letras a números
index_to_letter = dict(zip(range(len(alphabet)), alphabet)) # Establece el rando de número a letras


def matrix_mod_inv(matrix, modulus):
    """Encontramos el módulo de matriz inversa por medio de los siguientes pasos:
    Paso 1) Encuentra determinante
    Paso 2) Encuentre el valor determinante en un módulo específico (generalmente la longitud del alfabeto)
    Paso 3) Tome ese det_inv multiplicado por la matriz invertida det * (esta será la adjunta) en el módulo
    """

    det = int(np.round(np.linalg.det(matrix)))  # Paso 1)
    det_inv = egcd(det, modulus)[1] % modulus  # Paso 2)
    matrix_modulus_inv = (
        det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    )  # Paso 3)

    return matrix_modulus_inv


def encrypt(message, K):
    encrypted = ""
    message_in_numbers = []

    for letter in message:
        message_in_numbers.append(letter_to_index[letter]) #Proceso para transformar el mensaje en números

    split_P = [
        message_in_numbers[i : i + int(K.shape[0])]
        for i in range(0, len(message_in_numbers), int(K.shape[0])) 
    ]

    for P in split_P:
        P = np.transpose(np.asarray(P))[:, np.newaxis]

        while P.shape[0] != K.shape[0]:
            P = np.append(P, letter_to_index[" "])[:, np.newaxis]

        numbers = np.dot(K, P) % len(alphabet)
        n = numbers.shape[0]  # longitud del mensaje cifrado (en números)

        # Se regresa texto encriptado:
        for idx in range(n):
            number = int(numbers[idx, 0])
            encrypted += index_to_letter[number]

    return encrypted


def decrypt(cipher, Kinv):
    decrypted = ""
    cipher_in_numbers = []

    for letter in cipher:
        cipher_in_numbers.append(letter_to_index[letter])

    split_C = [
        cipher_in_numbers[i : i + int(Kinv.shape[0])]
        for i in range(0, len(cipher_in_numbers), int(Kinv.shape[0]))
    ]

    for C in split_C:
        C = np.transpose(np.asarray(C))[:, np.newaxis]
        numbers = np.dot(Kinv, C) % len(alphabet)
        n = numbers.shape[0]

        for idx in range(n):
            number = int(numbers[idx, 0])
            decrypted += index_to_letter[number]

    return decrypted


print("")
message2 = input("Ingrese el texto a cifrar: ")
message2 = message2.upper().strip().replace(" ", "")
print(f"Mensaje ingresado: {message2}")
print(f"Cantidad de letras: {len(message2)}")
b=len(message2)
c=b%2 
if c==0:
    print(message2)
    message=message2
    
    K = np.matrix([[1,7], [9, 2]])
    Kinv = matrix_mod_inv(K, len(alphabet))

    encrypted_message = encrypt(message, K)
    decrypted_message = decrypt(encrypted_message, Kinv)

    print(f"Mensaje original: " + message)
    print(f"Mensaje encriptado: " + encrypted_message)
    print(f"Mensaje desencriptado: " + decrypted_message) 

    tex=encrypted_message
    print(f"Texto ingresado:  {tex}")
    a_b = bytes(tex, "ascii")
    convertido=(''.join(["{0:b}".format(x)for x in a_b]))
    print(f"Texto convertido binario: {convertido}")
    d=convertido
    data=list(d)
    data.reverse()
    c,ch,j,r,h=0,0,0,0,[]

    while ((len(d)+r+1)>(pow(2,r))):
        r=r+1

    for i in range(0,(r+len(data))):
        p=(2**c)

        if(p==(i+1)):
            h.append(0)
            c=c+1

        else:
            h.append(int(data[j]))
            j=j+1

    for parity in range(0,(len(h))):
        ph=(2**ch)
        if(ph==(parity+1)):
            startIndex=ph-1
            i=startIndex
            toXor=[]

            while(i<len(h)):
                block=h[i:i+ph]
                toXor.extend(block)
                i+=2*ph

            for z in range(1,len(toXor)):
                h[startIndex]=h[startIndex]^toXor[z]
            ch+=1

    h.reverse()
    print('\nEl código Hamming generado es: ', end="")
    print(int(''.join(map(str, h))))
    print("\n")

    K = np.matrix([[1,7], [9, 2]])
    Kinv = matrix_mod_inv(K, len(alphabet))

    encrypted_message = encrypt(message, K)
    decrypted_message = decrypt(encrypted_message, Kinv)     

elif c!=0:
    message2+="Z"
    print(message2)
    message=message2
        
    K = np.matrix([[1,7], [9, 2]])
    Kinv = matrix_mod_inv(K, len(alphabet))

    encrypted_message = encrypt(message, K)
    decrypted_message = decrypt(encrypted_message, Kinv)

    print(f"Mensaje original: " + message)
    print(f"Mensaje encriptado: " + encrypted_message)
    nmen2=encrypted_message
    final_str2=nmen2[:-1]
    print(f"Corregido: mensaje encriptado: {final_str2}")
    print(f"Mensaje desencriptado: " + decrypted_message)
    nmen=decrypted_message
    final_str=nmen[:-1]
    print(f"Corregido: mensaje desencriptado: {final_str}")

    tex=final_str2
    print(f"Texto ingresado:  {tex}")
    a_b = bytes(tex, "ascii")
    convertido=(''.join(["{0:b}".format(x)for x in a_b]))
    print(f"Texto convertido binario: {convertido}")
    d=convertido
    data=list(d)
    data.reverse()
    c,ch,j,r,h=0,0,0,0,[]

    while ((len(d)+r+1)>(pow(2,r))):
        r=r+1

    for i in range(0,(r+len(data))):
        p=(2**c)

        if(p==(i+1)):
            h.append(0)
            c=c+1

        else:
            h.append(int(data[j]))
            j=j+1

    for parity in range(0,(len(h))):
        ph=(2**ch)
        if(ph==(parity+1)):
            startIndex=ph-1
            i=startIndex
            toXor=[]

            while(i<len(h)):
                block=h[i:i+ph]
                toXor.extend(block)
                i+=2*ph

            for z in range(1,len(toXor)):
                h[startIndex]=h[startIndex]^toXor[z]
            ch+=1

    h.reverse()
    print('\nEl código Hamming generado es: ', end="")
    print(int(''.join(map(str, h))))
    print("\n")


