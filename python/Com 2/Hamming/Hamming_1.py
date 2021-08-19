#### Victor Ortiz ####
option=int(input('\n *"Hamming" \n\nOpciones a realizar: \n\n 1. Generar codigo Hamming.  \n 2. Hallar error en el codigo Hamming.\n\nIngrese el número de la opción: '))

if(option==1):  # Para generar código Hamming 
    tex=input("\nIngrese el texto: ").upper().strip().replace(" ", "")
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

elif(option==2): # Para deterctar errores en Hamming
    print('Ingrese el código Hamming para detectar posibles errores: ')
    d=input()
    data=list(d)
    data.reverse()
    c,ch,j,r,error,h,parity_list,h_copy=0,0,0,0,0,[],[],[]

    for k in range(0,len(data)):
        p=(2**c)
        h.append(int(data[k]))
        h_copy.append(data[k])
        if(p==(k+1)):
            c=c+1
            
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
            parity_list.append(h[parity])
            ch+=1
    parity_list.reverse()
    error=sum(int(parity_list) * (2 ** i) for i, parity_list in enumerate(parity_list[::-1]))
    
    if((error)==0):
        print('No hay error en el código de Hamming ingresado.')

    elif((error)>=len(h_copy)):
        print('No se puede detectar el error')

    else:
        print(f'Se encontró error en la posición: {error}')

        if(h_copy[error-1]=='0'):
            h_copy[error-1]='1'

        elif(h_copy[error-1]=='1'):
            h_copy[error-1]='0'
            print('Después de la corrección, el código de Hamming es:')
        h_copy.reverse()
        print(int(''.join(map(str, h_copy))))
    print("\n")
else:
    print('\nLa opción que eligió no existe\n')