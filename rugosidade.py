import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.ticker import FuncFormatter



def grafico_rugosidade(W,titulo, modelo):
   
    Lconstante = 200;
    eixox ='Tempo (t)'
    eixoy = 'Rugosidade w(L,t)'

    plt.figure(figsize=(8,6))

    plt.title(titulo)
    plt.xlabel(eixox)
    plt.ylabel(eixoy)
    
    x1 = np.array(range(len(W[0])))
    y1 = W[0];
    plt.plot(x1,y1,label='L = 200')
    np.save('L200',W[0])

    x2 = np.array(range(len(W[1])))
    y2 = W[1];
    plt.plot(x2,y2,label='L = 400')
    np.save('L400ignore',W[1])

    x3 = np.array(range(len(W[2])))
    y3 = W[2];
    plt.plot(x3,y3,label='L = 800')
    np.save('L800ignore',W[2])

    x4 = np.array(range(len(W[3])))
    y4 = W[3];
    plt.plot(x4,y4,label='L = 1600')
    np.save('L1600ignore',W[3])
       
    """arquivo_new = open("coordenadas.txt","w")
    for i in y4:
        arquivo_new.write('{0}\n'.format(i));
    arquivo_new.close()
    """
    #'linear', 'log', 'symlog', 'logit', 'function', 'functionlog'
    plt.legend()
    plt.yscale('log')
    #plt.ylim(ymax=sorted(y4)[-1]+1000,ymin=sorted(y4)[0]-1)
    plt.xscale('log')

    #plt.show()
    plt.savefig('data/{0}/rugosidade_{0}.png'.format(modelo), dpi=300)
    plt.cla()
    plt.clf()
    plt.close()
