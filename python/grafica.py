import matplotlib.pyplot as plt
from numpy import arange,sin,pi
x=arange(0.0, 2*pi, 0.01)
y=sin(x)
plt.plot(x,y)
plt.grid(axis='both')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')
plt.show()