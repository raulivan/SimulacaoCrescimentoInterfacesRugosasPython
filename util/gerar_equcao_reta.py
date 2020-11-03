"""
A equacao da reta e dada por y = mx + b

 Onde:

 m e o coeficiente angular da reta (determina a sua inclinacao)
 b e o coeficiente linear da reta e determina o ponto onde a
 reta corta o eixo y (isto e, b determina o valor de y quando x for zero)
"""
from fractions import Fraction

print("Determinacao da equacao da reta a partir de 2 pontos:")
x1 = '1'
y1 = '0.9250521028757385'

x2 = '9999'
y2 = '13.375926991635836'

print("(x1, y1) = (%s, %s)" % (x1, y1))
print("(x2, y2) = (%s, %s)" % (x2, y2))

x1Frac = Fraction(x1)
y1Frac = Fraction(y1)

x2Frac = Fraction(x2)
y2Frac = Fraction(y2)

mFrac = (y2Frac - y1Frac) / (x2Frac - x1Frac)

bFrac = y1Frac - (mFrac*x1Frac)

print("Equacao geral da reta: y = mx+b")

sign = ""
if bFrac > 0:
    sign = "+"

# Monta m e b em formato string levando em consideracao se o
# denominador for igual a 1 (se denominador=1, nao mostra fracao)
if mFrac.denominator == 1:
    mStr = "%d" % mFrac.numerator
else:
    mStr = "(%d/%d)" % (mFrac.numerator, mFrac.denominator)

if bFrac.denominator == 1:
    bStr = "%d" % bFrac.numerator
else:
    bStr = "(%d/%d)" % (bFrac.numerator, bFrac.denominator)

print("\nEquacao da reta proposta: y=%sx%s%s" % (mStr,sign,bStr))

print("Coeficiente angular: %s" % mStr.strip("(").strip(")"))
print("Coeficiente linear: %s" % bStr.strip("(").strip(")"))