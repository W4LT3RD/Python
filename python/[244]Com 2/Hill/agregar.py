a=input("Ingrese texto: ")
print(f"Cantidad de letras: {len(a)}")
b=len(a)
c=b%2 
if c==0:
    print(a)
elif c!=0:
    a+="ñ"
    print(a)
print(a)
print(a[:-1])
