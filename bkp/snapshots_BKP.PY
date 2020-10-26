import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd

"""
L200 = np.load('substratoL200.npy')

x = np.array(range(len(L200)))
y = L200

titulo = 'Interface DA'
eixox = 'Sitio (i)'
eixoy = 'Altura (h)'

plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

#plt.bar(x,y)
plt.hist(y, bins=10, histtype='step', linewidth=2, facecolor='c', 
         hatch='/', edgecolor='k',fill=True)
# plt.savefig(titulo + '.png', dpi=300)
plt.show()
"""
"""
# set seed for reproducing
np.random.seed(42)
n = 5000
mean_mu1 = 60
sd_sigma1 = 15
data11 = np.random.normal(mean_mu1, sd_sigma1, n)
mean_mu2 = 80
sd_sigma2 = 15
data22 = np.random.normal(mean_mu2, sd_sigma2, n)
"""


titulo = 'Interface DA'
eixox = 'Sitio (i)'
eixoy = 'Altura (h)'

L200Parte1 = np.load('data/da/substratoL20Part1.npy')
L200Parte2 = np.load('data/da/substratoL20Part2.npy')
L200Parte3 = np.load('data/da/substratoL20Part3.npy')
L200Parte4 = np.load('data/da/substratoL20Part4.npy')

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
plt.savefig(titulo + '.png', dpi=300)

# plt.show()