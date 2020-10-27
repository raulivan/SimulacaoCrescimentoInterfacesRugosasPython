import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.ticker import FuncFormatter

modelo = 'db'

plt.figure(figsize=(8,6))

plt.title('Deposição Balística')
plt.xlabel('Tempo (t)')
plt.ylabel('Rugosidade w(L,t)')


y4_data = np.load('grafico/saturacao/{0}/L1600.npy'.format(modelo));
y4 = y4_data[0:10**6 - 10*3]
x4 = np.array(range(len(y4)))
plt.plot(x4,y4,label='L = 1600')

y3_data = np.load('grafico/saturacao/{0}/L800.npy'.format(modelo));
y3 = y3_data[0:10**5 - 10*3]
x3 = np.array(range(len(y3)))
plt.plot(x3,y3,label='L = 800')

y2_data =  np.load('grafico/saturacao/{0}/L400.npy'.format(modelo));
y2 = y2_data[0:(10**4 - 10*3)]
x2 = np.array(range(len(y2)))
plt.plot(x2,y2,label='L = 400')

y1_data = np.load('grafico/saturacao/{0}/L200.npy'.format(modelo));
y1 = y1_data[0:10**3]
x1 = np.array(range(len(y1)))
plt.plot(x1,y1,label='L = 200')

plt.legend()
plt.yscale('log')
plt.xscale('log')

#plt.show()
plt.savefig('data/DB/rugosidade_DB.png', dpi=300)
plt.cla()
plt.clf()
plt.close()
