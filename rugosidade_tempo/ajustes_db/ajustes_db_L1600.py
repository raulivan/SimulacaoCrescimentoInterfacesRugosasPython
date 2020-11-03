import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.ticker import FuncFormatter

def funcao_linear(x):
    #return 0.001427 * x - 0.00054
    return 0.001427 * x - 0.00054

modelo = 'db'
plt.figure(figsize=(8,6))

plt.title('DB L = 1600')

plt.xlabel('t')
plt.ylabel('w(L,t)')

y = np.load('grafico/saturacao/{0}/L200.npy'.format(modelo));
x = np.array(range(len(y)))
passo = 1 # round(len(y) / 200,0) 

contador = 0
media_x=[]
media_y=[]
tempo = 0

while(contador < len(y)):
    media_x.append(contador)
    valor = y[int(contador)]
    media_y.append(valor)
    contador = contador + passo
    
subida_x = []
subida_y = []
for t in media_x[0:7]:
    subida_x.append(t)
    subida_y.append(funcao_linear(t))

z = np.polyfit(subida_x,subida_y,1)
equacao = np.poly1d(z)
print("Best fit polinomial equation: ",equacao)

plt.plot( media_x, media_y, 'go') # green bolinha
# plt.plot( subida_x,  equacao(subida_y), 'k:', color='orange') # linha pontilha orange


plt.yscale('log')
plt.xscale('log')

plt.show()
# plt.savefig('data/DARS/rugosidade_ajuste_DARS_L1600.png', dpi=300)
plt.cla()
plt.clf()
plt.close()

"""
b = 0,001427
"""