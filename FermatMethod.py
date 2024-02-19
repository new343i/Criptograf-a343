import math
from random import randint
import random
import sys

class FermatMethod:
    def __init__(self, n):
        self.n = n
        self.x = []  # Inicializar la lista x
    
#Test de enteros
    def testInt(self, b):
        return b.is_integer() and b > 1

    #Test de multiplos
    def multi(self, n, multiplo):
        return n % multiplo == 0

    #Test de primalidad en base a Fermat
    def testPrim(self):
        for _ in range(1, 20):
            a = randint(1, self.n - 1)
            nummult = pow(a, self.n - 1, self.n) - 1
            if self.multi(nummult, self.n) == True:
                return True
        return False  # Retorna False después de todas las iteraciones

    
       # Test de primalidad en base a Rabin-Miller
    def Rabin(self, n, k=7):
        if n < 2:
            return False
        if n < 4:
            return True
        if n % 2 == 0:
            return False

        # Descomponer n - 1 en la forma (2^s) * d
        s, d = 0, n - 1
        while d % 2 == 0:
            s += 1
            d //= 2

        # Realizar las iteraciones de Rabin-Miller
        for _ in range(k):
            a = random.randint(2, n - 2)
            x = pow(a, d, n)

            if x == 1 or x == n - 1:
                continue

            for _ in range(s - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False

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

     # Sacar el máximo de primos
    def sacaMOPM(self, n):
        for num in n:
            if isinstance(num, int):
                if self.Rabin(num):
                    self.x.append(num)
                else:
                    factors = self.factFermat(num)
                    self.x.extend(factors)

        return self.x if self.x else "No se encontraron factores primos"