# Operador lógicos
"""
    AND (Conjunción)    and
    OR (Disyunción)     or
    NOT (Negación)      not
"""
# Prioridad de operadores en general:
"""
    1. ()
    2. **
    3. *, /, %, not
    4. +, -, and 
    5. >, <, ==, >=, <=, =!, or
"""
print("_____________________________________\n")
print("a=5, b=3, c=8")
a=5
b=3
c=8
res1=((a<b)and(b==c)or(c>a))
print("(a<b)and(b==c)or(c>a) \n",res1)