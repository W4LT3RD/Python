import socket

mi_socket = socket.socket()
mi_socket.bind(("localhost", 8000))
mi_socket.listen(5)

while true:
    conexion, addr = mi_socket.accept()
    print("Conexión establecida")
    print(addr)

    peticion = conexion.recv(1024)
    print(peticion)

    conexion.send("Hola desde el sevidor.")
    conexion.close