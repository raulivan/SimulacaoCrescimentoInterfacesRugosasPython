import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.ticker import FuncFormatter

w200 = np.load('data/da/rugosidade20.npy')

x = np.array(range(len(w200)))
y = w200

print(y);

titulo = 'Deposição Aleatória'
eixox ='Tempo (t)'
eixoy = 'Rugosidade w(L,t)'

plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.plot(x,y,label='Substrato {0}'.format(200))
plt.legend()
plt.yscale('log')
plt.xscale('log')

plt.show()
# plt.savefig('data/da/' + titulo + '.png', dpi=300)
