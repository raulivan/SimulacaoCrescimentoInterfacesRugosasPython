import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.ticker import FuncFormatter

modelo = 'dars'

plt.figure(figsize=(8,6))

plt.title('Deposição Aleatória com Relaxação Superficial')
plt.xlabel('Tempo (t)')
plt.ylabel('Rugosidade w(L,t)')

y4 = np.load('grafico/saturacao/{0}/L1600.npy'.format(modelo));
x4 = np.array(range(len(y4)))
plt.plot(x4,y4,label='L = 1600')

y3 = np.load('grafico/saturacao/{0}/L800.npy'.format(modelo));
x3 = np.array(range(len(y3)))
plt.plot(x3,y3,label='L = 800')

y2 =  np.load('grafico/saturacao/{0}/L400.npy'.format(modelo));
x2 = np.array(range(len(y2)))
plt.plot(x2,y2,label='L = 400')

y1 = np.load('grafico/saturacao/{0}/L200.npy'.format(modelo));
x1 = np.array(range(len(y1)))
plt.plot(x1,y1,label='L = 200')

plt.legend()
plt.yscale('log')
plt.xscale('log')

#plt.show()
plt.savefig('data/DARS/rugosidade_DARS.png', dpi=300)
plt.cla()
plt.clf()
plt.close()
