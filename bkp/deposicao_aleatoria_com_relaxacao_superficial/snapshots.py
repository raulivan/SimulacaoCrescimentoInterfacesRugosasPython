import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd

titulo = 'Interface DARS'
eixox = 'Sitio (i)'
eixoy = 'Altura (h)'

L200Parte1 = np.load('data/dars/substratoL20Part1.npy')
L200Parte2 = np.load('data/dars/substratoL20Part2.npy')
L200Parte3 = np.load('data/dars/substratoL20Part3.npy')
L200Parte4 = np.load('data/dars/substratoL20Part4.npy')

x = np.array(range(len(L200Parte1)))
y1 = L200Parte1
y2 = L200Parte2
y3 = L200Parte3
y4 = L200Parte4


plt.figure(figsize=(8,6))


plt.xlabel(eixox, size=14)
plt.ylabel(eixoy, size=14)
plt.title(titulo)

plt.bar(x,y1, color='b',alpha=1)
plt.bar(x,y2,color='g',alpha=0.8)
plt.bar(x,y3,color='r',alpha=0.5)
plt.bar(x,y4,color='k',alpha=0.3)


# plt.legend(loc='upper right')
# plt.savefig(titulo + '.png', dpi=300)

plt.show()