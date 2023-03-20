import math
import sys
from random import randint
import random
from time import time

def Rabin(n, k = 7):
    if n < 6:  # asumiendo n >= 0 en todos los casos ... pequeño atajo de casos aquí
        return [False, True, True, True, False, True][n]
    elif n & 1 == 0:  # Debería ser más rápido que n % 2
        return False
    else:
        s, d = 0, n - 1
        while d & 1 == 0:
            s, d = s + 1, d >> 1
    # Utilice random.randint (2, n-2) para números muy grandes
        for a in random.sample(range(2, min(n - 2, sys.maxsize)), min(n - 4, k)):
            x = pow(a, d, n)
            if x != 1 and x + 1 != n:
                for r in range(1, s):
                    x = pow(x, 2, n)
                    if x == 1:
                        return False  # compuesto seguro
                    elif x == n - 1:
                        a = 0  # entonces sabemos que el bucle no continuó hasta terminar
                        break  # Podría ser un Falso fuerte, prueba con otro a
                if a:
                    return False  # Compuesto si llegamos al final de este bucle
        return True

def testPrim(self):
    for i in range(1, 20):
        a=randint(1, self.n-1)
        nummult=pow(a, self.n-1) - 1
        if self.multi(nummult, self.n) == True:
            return True
        else:
            return False

def testInt(b):
    bround=round(b)
    terminal=b-bround
    if terminal == 0:
        return True
    else:
        return False

def factFermath(n):
    k=int(math.floor(math.sqrt(n))) + 1
    y=(k*k) - n
    d = 1
    print(k, y, n)
    if int(math.floor(math.sqrt(y))) == math.sqrt(y):
        x = math.sqrt(n + y)
        y = math.sqrt(y)
        fact1 = x - y
        fact2 = x + y
        return fact1, fact2
    else:
        y = y + 2*k + d
        d = d + 2
    print(k, y, d)
    while int(math.floor(math.sqrt(y))) < n / 2:
        if int(math.floor(math.sqrt(y))) == math.sqrt(y):
            x = math.sqrt(n + y)
            y = math.sqrt(y)
            fact1 = x - y
            fact2 = x + y
            #print(x, y)
            return fact1, fact2
        else:
            y = y + 2*k + d
            d = d + 2
        print(k, y, d)

def factFermath1(n):
    a=int(math.floor(math.sqrt(n))) + 1
    Bcuad=(a*a) - n
    if Bcuad < 0:
        Bcuad=Bcuad*(-1)
    bN=math.sqrt(Bcuad)
    while testInt(bN) == False:
        bN=math.sqrt(Bcuad)
        a=a+1
        Bcuad=a*a-n
        bN=math.sqrt(Bcuad)        
    fact1=a - math.sqrt(Bcuad)
    fact2=a + math.sqrt(Bcuad)
    #print(a, Bcuad, bN, nimp)
    return fact1, fact2


#Sacar El maximo de Primos
def sacaMOPM(n):
    n2 = []
    if n != None:
        for i in range(0, len(n)):
            n2.append(n[i])
            t=Rabin(int(n2[i]))
            if t == True:
                x.append(n2[i])
            else:
                sacaMOPM(factFermath(int(n2[i])))
    else:
        print("No se ecnontraron factores")
#T1 = time()
#x = []
n=278153
n1 = 12345
#print(sacaMOPM(factFermath(int(n))))
#T2 = time()
#TF = T2 - T1
#print(x)
#print(TF)

T1F = time()
x = []
#print(factFermath(int(n)))
sacaMOPM(factFermath(int(n)))
T2F = time()
TFF = T2F - T1F
print(x)
print(TFF)

