import math
from random import randint
import random
import sys
class FermatMethod:
    def __init__(self, n):
        self.n=n
    
#Test de enteros
    def testInt(self,b):
        bround=round(b)
        terminal=b-bround
        if terminal == 0:
            return True
        else:
            return False

    #Test de multiplos
    def multi(self, n, multiplo):
        return n % multiplo == 0

    #Test de primalidad en base a Fermat
    def testPrim(self):
        for i in range(1, 20):
            a=randint(1, self.n-1)
            nummult=pow(a, self.n-1) - 1
            if self.multi(nummult, self.n) == True:
                return True
            else:
                return False

    #Test de primalidad en base a Rabin-Miller
    def Rabin(self, n, k = 7):
        if n < 6:  # asumiendo n >= 0 en todos los casos ... pequeño atajo de casos aquí
            return [False, False, True, True, False, True][n]
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

    #Determinar si es impar
    def deterPar(self):
        if self.multi(self.n, 2) == True:
            return False
        else:
            return True

    #Factorizar mediante Fermat
    def factFermat(self, n):
        k=int(math.floor(math.sqrt(n))) + 1
        y=(k*k) - n
        #print(k)
        d = 1
        #Y = int(math.floor(math.sqrt(y)))
        #print(Y == math.sqrt(y))
        while int(math.floor(math.sqrt(y))) < n / 2:
            if int(math.floor(math.sqrt(y))) == math.sqrt(y):
                x = math.sqrt(n + y)
                y = math.sqrt(y)
                fact1 = x - y
                fact2 = x + y
                #print(fact1 , " " , fact2)
                return fact1, fact2
            else:
                y = y + 2*k + d
                d = d + 2

    #Sacar El maximo de Primos
    def sacaMOPM(self, n):
        if n != None:
            for i in range(0, len(n)):
                t=self.Rabin(int(n[i]))
                if t == True:
                    #print(n[i])
                    self.x.append(n[i])
                    #print(x)
                else:
                    self.sacaMOPM(self.factFermat(int(n[i])))
        else:
            return "No se encontraron factores"

    x = []
