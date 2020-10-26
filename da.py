import random
import numpy as np
import math
import sympy as sym
from tqdm import tqdm, trange
from snapshots import snapshots_interface, snapshots_interface_camadas
from rugosidade import grafico_rugosidade

print('Deposição Aleatória')
np.warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)

# Funções necessárias
def aleatorio(L):
    # passo 1
    min = 2**31;
    min = min * -1;
    max = 2**31;
    x = random.randint(min,max);
    # passo 2
    x = x if x >= 0 else x * -1
    # passo 3
    x = ((L - 1)/max) * x
    # passo 4
    x = int(round(x,0));
    return x

def numero_aleatorio(L):
    x = random.randint(0,(L  - 1));
    return x

def altura_media(L):
    divisao = 1 / len(L)
    somatorio = 0
    for i in L:
        somatorio = somatorio + i
    altura_media = divisao * somatorio
    return altura_media

def rugosidade_w(L):
    w = 0
    somatorio = 0
    h_media = altura_media(L)
    divisao = 1 / len(L)

    for h in L:
        diff = h - h_media
        diff = diff ** 2
        somatorio = somatorio + diff
    
    w = divisao * somatorio
    w = math.sqrt(w)

    return w
def quebra_grafico(L,t, Tmax):
    caminho = 'grafico/da/'
    q = round(Tmax / 4,0)
    if(t == q):
        np.save('{0}parte1{1}.npy'.format(caminho,(len(L)-1)),L)
    elif(t == (q*2)):
        np.save('{0}parte2{1}.npy'.format(caminho,(len(L)-1)),L)
    elif(t == (q*3)):
        np.save('{0}parte3{1}.npy'.format(caminho,(len(L)-1)),L)
    elif(t == (Tmax-1)):
        np.save('{0}parte4{1}.npy'.format(caminho,(len(L)-1)),L)

def deposicao(L,W,Tmax):
    # barra de progresso
    with tqdm(total=Tmax) as pbar: 
        # percorrendo o tempo máximo para deposição
        for t in range(Tmax):
            # fazendo a deposição de Len(L) particulas
            for particula in range(len(L)):
                # sorteia um sitio para deposito entre 0 e len(L)
                sitio = numero_aleatorio(len(L))
                # incrementa a altura do sitio selecionado
                L[sitio] = L[sitio] + 1

            # calculando a rugosidade no tempo t  
            if (t > 0):    
                W[t] = rugosidade_w(L)
                if W[t] < 0:
                    W[t] = W[t] * -1
            else:
                W[t] = 0
            #quebra_grafico(L,t,Tmax)
            pbar.update(1)

# Parâmetros
#Tmax = 10**4 # tempo máximo
N = 10**3 # número de amostras
L200 = 200 # Substrato de tamanho 200
L400 = 400 # Substrato de tamanho 400
L800 = 800 # Substrato de tamanho 800
L1600 = 1600 # Substrato de tamanho 1.600

substratosL = np.array([np.zeros(L200+1),
                        np.zeros(L400+1),
                        np.zeros(L800+1),
                        np.zeros(L1600+1)])

Tmax = np.array([10**1, 10**2, 10**3, 10**4])

rugosidadeW = np.array([np.zeros(Tmax[0]),
                        np.zeros(Tmax[1]),
                        np.zeros(Tmax[2]),
                        np.zeros(Tmax[3])])

# Realização da simulação de deposição

# barra de progresso
numero_substratos = len(substratosL)
with tqdm(total=numero_substratos) as pbar: 
    # percorrendo cada substrato para deposição, L = 200, 400, 800 E 1600 
    for i in range(numero_substratos):
        deposicao(substratosL[i],rugosidadeW[i],Tmax[i])
        #snapshots_interface_camadas(substratosL[i],'Rede de comprimento L = {0}'.format(len(substratosL[i])-1),'DA')
        pbar.update(1)

grafico_rugosidade(rugosidadeW,'Deposição Aleatória','DA')

