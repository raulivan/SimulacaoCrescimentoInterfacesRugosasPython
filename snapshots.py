import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd
import itertools

def snapshots_interface(L, titulo, modelo):
    eixox = 'i'
    eixoy = 'h'

    x = np.array(range(len(L)))

    plt.figure(figsize=(8,6))
    

    plt.xlabel(eixox, size=14)
    plt.ylabel(eixoy, size=14)
    plt.title(titulo)

    colors = itertools.cycle(["r", "b", "g"])
    plt.plot(x,L, color='b',alpha=0.5)


    plt.savefig('data/{0}/snapshots_interface_{0}_L{1}.png'.format(modelo,len(L)-1), dpi=300)
    plt.cla()
    plt.clf()
    plt.close()
    #plt.show()


def snapshots_interface_camadas(L, titulo, modelo):
    eixox = 'i'
    eixoy = 'h'
    plt.figure(figsize=(8,6))
    
    x = np.array(range(len(L)))
    y1=[]
    y2=[]
    y3=[]
    y4=[]

    sub = len(L) -1
    if (modelo == 'DA'):
        y1 = np.load('grafico/da/parte1{0}.npy'.format(sub))
        y2 = np.load('grafico/da/parte2{0}.npy'.format(sub))
        y3 = np.load('grafico/da/parte3{0}.npy'.format(sub))
        y4 = np.load('grafico/da/parte4{0}.npy'.format(sub))
    elif (modelo == 'DARS'):
        y1 = np.load('grafico/dars/parte1{0}.npy'.format(sub))
        y2 = np.load('grafico/dars/parte2{0}.npy'.format(sub))
        y3 = np.load('grafico/dars/parte3{0}.npy'.format(sub))
        y4 = np.load('grafico/dars/parte4{0}.npy'.format(sub))
    elif (modelo == 'DB'):
        y1 = np.load('grafico/db/parte1{0}.npy'.format(sub))
        y2 = np.load('grafico/db/parte2{0}.npy'.format(sub))
        y3 = np.load('grafico/db/parte3{0}.npy'.format(sub))
        y4 = np.load('grafico/db/parte4{0}.npy'.format(sub))
    

    plt.xlabel(eixox, size=14)
    plt.ylabel(eixoy, size=14)
    plt.title(titulo)

    colors = itertools.cycle(["r", "b", "g"])
    plt.plot(x,y1, color='r',alpha=0.5)
    plt.plot(x,y2, color='g',alpha=0.5)
    plt.plot(x,y3, color='b',alpha=0.5)
    plt.plot(x,y4, color='y',alpha=0.5)


    plt.savefig('data/{0}/snapshots_interface_{0}_L{1}.png'.format(modelo,len(L)-1), dpi=300)
    plt.cla()
    plt.clf()
    plt.close()
    #plt.show()


    """
    https://medium.com/horadecodar/gráficos-de-barra-com-matplotlib-85628bfc4351
    """