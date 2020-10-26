import random
import numpy as np
import math
import sympy as sym
from tqdm import tqdm, trange

print('Deposição aleatória com relaxação superficial')

#Variáveis global
# Tempo de máximo de execução
Tmax = 10**6

# Substrato de tamanho 200
L200 = 200
L400 = 400
L800 = 800
L1600 = 1600

nRelaxamento = 10;
N = 2 #10**3

# Matriz com os calculos da rugosidade
vRugosidade = np.array([np.zeros(L200)])  
sem = 123456789

# altura minima
def Min(passo, altura,):
    # Default
    Result = passo
   
    if (altura[passo] == 0): return;

    lResult = passo
    rResult = passo;

    #contador de relaxamento
    nPos = 1

    # olhando a esquerda
    while (nPos <= nRelaxamento) or ((passo - nPos) >= 0):
        if (altura[passo -nPos] == 0 or altura[passo - nPos < altura[passo] + 1]):
            lResult = passo - nPos
        elif (altura[passo - nPos] > altura[passo] + 1):
            lResult = passo
        else:
            passo - nPos
        if altura[lResult] == 0: 
            break
        nPos = nPos + 1 
    
    # olhando a direita
    while (nPos <= nRelaxamento or (passo + nPos) <= len(altura)):
        if (altura[passo - nPos] == 0 or altura[passo + nPos] < altura[passo] + 1):
            rResult = passo + nPos
        elif (altura[passo + nPos] > altura[passo] + 1):
            rResult = passo
        else:
            rResult = passo + nPos
        if (altura[lResult] == 0):
            break
        nPos = nPos + 1
    
    if (altura[lResult] == altura[rResult]):
        Result = rResult
    elif (altura[lResult] < altura[rResult]):
        Result = lResult
    else:
        Result = rResult
    
    return Result

# altura máxima
def Max(index,altura, tamanho):
    Result = 0
    if (index < 0):
        Result = altura[0]
    elif (index > len(altura) - 1):
        Result = altura[tamanho -1]
    else:
        Result = altura[index]
    
    return Result

# Calcular a Media da Altura
def Media(index,altura):
    Result = 0.0
    if(index == 0):
        Result = (Result + altura[0])
    else:
        Result = Media(index - 1,altura) + altura[index]
    return Result

# Calcular Rugosidade
def Rugosidade(index,altura):
    Result = 0.0
    if (index == -1): return

    Result = Rugosidade(index - 1, altura) + math.pow(cAlturaMedia - altura[index],2)

    return Result

def aleat(sem1):
    M = 1073741824
    A = 843314861
    B = 453816693

    aux = 0.0
    xx = 0.0

    aux = 0.5 / (1.0 * M)
    sem1 = sem1 * A + B
    if (sem1 < 0):
        sem1 = (sem1 + M) + M
    xx = 1.0 * aux * sem1
    sem = sem1
    
    return xx
"""
# Gerar os experimentos...
def DA(nExperimento, nParticula, tamanho):
    i = 0
    passo = 0
    altura = []

    sem = 123456789;
    vRugosidade =  np.array([np.zeros(nExperimento), np.zeros(nParticula)])
    
          try

              // cria a i-�sima linha da matriz dinamicamente
              SetLength(vRugosidade[nExperimento], nParticula);
              // Declarar uma matriz dinamicamente
              SetLength(altura, L );
              if (nParticula <= 0) then Exit;
          except
              Application.MessageBox(
                          'Por favor, informe o n�mero de experimentos...',
                          'Informa��o',  mb_iconinformation + mb_ok);
              Exit;
          end;
          // Default ( Altura );
          for i := 0 to L - 1 do begin
              Altura[i] := 0;
          end;
          // Gerar a DA
          for i := 0 to nParticula - 1 do  begin
              // Gerar n�umero aleat�rio
              Passo := Trunc(aleat(sem) * L);
              // Posi��o Minima
              Passo := Min(Passo, Altura);
              // Atualizar a altura Min....
              Altura[Passo] := Altura[Passo] + 1;
              // Calcula Media da Altura...
              cAlturaMedia := (Media(L - 1,Altura)) / L;
              // Calcular a Rugosidade
              vRugosidade[nExperimento, i] :=
                          Sqrt(Rugosidade(Length(Altura) - 1, Altura) / L);
          end;
end;

# Constantes
# M = 1073741824; #máximo, usado pra gerar num aleatorio
# A = 843314861; #usado pra gerar num aleatorio
AA = 65539;
# B = 453816693; #usado pra gerar num aleatorio
H = 10000000;
nRelaxamento = 10;
# L = tamanho = 200





vRugosidade = np.zeros(Tmax)
cAlturaMedia =  0.0


"""
print(vRugosidade.shape);

