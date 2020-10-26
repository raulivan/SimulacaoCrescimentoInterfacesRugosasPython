import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.ticker import FuncFormatter

modelo = 'db'

plt.figure(figsize=(8,6))

plt.title('Deposição Balística')
plt.xlabel('Tempo (t)')
plt.ylabel('Rugosidade w(L,t)')

y1_data = np.load('grafico/saturacao/{0}/L200.npy'.format(modelo));
y1 = y1_data[0:10**3]
x1 = np.array(range(len(y1)))
plt.plot(x1,y1,label='L = 200')

y2_data =  np.load('grafico/saturacao/{0}/L400.npy'.format(modelo));
y2 = y2_data[0:10**4]
x2 = np.array(range(len(y2)))
plt.plot(x2,y2,label='L = 400')

y3_data = np.load('grafico/saturacao/{0}/L800.npy'.format(modelo));
y3 = y3_data[0:10**5]
x3 = np.array(range(len(y3)))
plt.plot(x3,y3,label='L = 800')

"""
y4 = np.load('grafico/saturacao/{0}/L1600.npy'.format(modelo));
x4 = np.array(range(len(y4)))
plt.plot(x4,y4,label='L = 1600')
"""
"""
arquivo_new = open("coordenadas.txt","w")
for i in y4:
    arquivo_new.write('{0}\n'.format(i));
arquivo_new.close()
"""
#'linear', 'log', 'symlog', 'logit', 'function', 'functionlog'
plt.legend()
plt.yscale('log')
#plt.ylim(ymax=sorted(y3)[-1]+1000,ymin=sorted(y3)[0]-1)
plt.xscale('log')

plt.show()
#plt.savefig('data/{0}/rugosidade_{0}.png'.format('DARS'), dpi=300)
plt.cla()
plt.clf()
plt.close()
