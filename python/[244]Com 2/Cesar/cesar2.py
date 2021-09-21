L2I = dict(zip("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ",range(26)))
I2L = dict(zip(range(26),"ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"))
key = 3 # corrimiento de bits

text=input("\nIngrese el texto a cifrar: ").upper()
plaintext=text
ciphertext = ""
for c in plaintext.upper():
    if c.isalpha(): 
        ciphertext += I2L[ (L2I[c] + key)%26 ]
    else: 
        ciphertext += c
print (f"Texto Cifrado: {ciphertext}")

tex=ciphertext.upper().strip().replace(" ", "")
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