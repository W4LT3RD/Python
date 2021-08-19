#   Operadores de asignación
"""
    Primero crear la variable o variables con las que se van a trabajar.

    a += b, Suma en asignació
    b -= c, resta en asignación
    c *= d, multiplicación en asignación
    d /= e, divisi0243n en asignación
    e **= f, potencia en asignación 
    f %= g, módulo en asignación 
"""
print("________________________________________________\n")
a=4
print("a = ",a)
a+=4
print("a+=4  = ",a)
a-=2
print("a-=2 = ", a)
a*=3
print('a*=3 = ',a)
a*=5
print("a*=5 = ",a)
a/=9
print("a/=9 = ",a)
a%=5 # a=10 -> 10/5 .: residuo = 0
print("a%=5 = ", a, "<- residuo de 10/5")