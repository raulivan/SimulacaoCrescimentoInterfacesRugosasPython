import random
import numpy as np
import math
import sympy as sym
from tqdm import tqdm, trange

print('Deposição aleatória')

def numeroAleatorio(L):
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

def calcAlturaMedia(L):
    divisao = 1 / len(L)
    somatorio = 0
    for i in L:
        somatorio = somatorio + i
    altura_media = divisao * somatorio
    return altura_media

def calRugosidade(L):
    w = 0
    somatorio = 0
    altura_media = calcAlturaMedia(L)
    divisao = 1 / len(L)

    for h in L:
        diff = h - altura_media
        diff = diff ** 2
        somatorio = somatorio + diff
    
    w = divisao * somatorio
    w = math.sqrt(w)

    return w

def deposicao(Tmax, tamanho):
    print('DA - L = ' + str(tamanho))
    substratoL = np.zeros(tamanho)
    rugosidadeW = np.zeros(Tmax)

    with tqdm(total=Tmax) as pbar:
        for t in range(Tmax):
            for p in range(tamanho):
                i = numeroAleatorio(tamanho)
                substratoL[i] = substratoL[i] + 1
            rugosidadeW[t] = calRugosidade(substratoL)
            if rugosidadeW[t] < 0:
                rugosidadeW[t] = rugosidadeW[t] * -1
            pbar.update(1)
            if(t == 2500):
                np.save('data/da/substratoL' + str(tamanho) + 'Part1.npy',substratoL)
            elif(t == 5000):
                np.save('data/da/substratoL' + str(tamanho) + 'Part2.npy',substratoL)
            elif(t == 7500):
                np.save('data/da/substratoL' + str(tamanho) + 'Part3.npy',substratoL)
            elif(t == (Tmax -1)):
                np.save('data/da/substratoL' + str(tamanho) + 'Part4.npy',substratoL)

    np.save('data/da/substratoL' + str(tamanho) + '.npy',substratoL)
    np.save('data/da/rugosidade' + str(tamanho) + '.npy',rugosidadeW)


# Tempo de máximo de execução
Tmax = 10**4

# Substrato de tamanho 200
deposicao(Tmax, 20)






