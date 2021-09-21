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
from egcd import egcd 

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
b=len(message2)
c=b%2 
if c==0:
    message=message2
    K = np.matrix([[1,7], [9, 2]])
    Kinv = matrix_mod_inv(K, len(alphabet))

    encrypted_message = encrypt(message, K)
    decrypted_message = decrypt(encrypted_message, Kinv)

    print(f"Mensaje original: " + message)
    print(f"Mensaje encriptado: " + encrypted_message)
    print(f"Mensaje desencriptado: " + decrypted_message) 


    K = np.matrix([[1,7], [9, 2]])
    Kinv = matrix_mod_inv(K, len(alphabet))

    encrypted_message = encrypt(message, K)
    decrypted_message = decrypt(encrypted_message, Kinv)     

elif c!=0:
    message2+="Z"
    message=message2
        
    K = np.matrix([[1,7], [9, 2]])
    Kinv = matrix_mod_inv(K, len(alphabet))

    encrypted_message = encrypt(message, K)
    decrypted_message = decrypt(encrypted_message, Kinv)

    print(f"Mensaje original: " + message[:-1])
    print(f"Mensaje encriptado: ", encrypted_message[:-1])

    print(f"Mensaje desencriptado: " + decrypted_message[:-1])

