class Ascii():
    def __init__(self):
        pass
    
    def ascii(self, caracter):
        return ord(caracter)
    
    def caracter(self, ascii):
        return chr(ascii)

obj = Ascii()
a=input("Ingrese el texto: ")
print(obj.ascii(a))

