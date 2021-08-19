import numpy as np
import matplotlib.pyplot as plt
import math 

dat = np.array ([2.5, 8.2, -1.1, -0.2, 1.5])
print('Datos: \n',dat)

med = np.mean(dat)
var = np.var(dat)
desv = np.std(dat)
pot_med = np.mean((dat)**2)
mag_med = np.mean(np.abs(dat))
print('___________________________________ \n')

print('Media: %f' % med)
print('Desviación Estándar: %f' % desv)
print('Varianza: %f' % var)
print('Potencia media: %f' % pot_med)
print('Magnitud media: %f' % mag_med)

print('___________________________________ \n')

zero_crossings2 = np.where(np.diff(np.sign(dat)))[0]  
print ('Cruces de cero: %f' % len(zero_crossings2))

print('___________________________________ \n')

plt.subplot(2,1,1)
plt.plot(dat)
plt.grid(axis='both')
plt.xlabel('Señal de voz')
plt.show()
