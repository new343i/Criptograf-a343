import sys
from random import randint
import random
from math import gcd
from time import time
class PollardsMethod:
    def __init__(self, n, a):
        self.n = n
        self.a = a
        
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

    def oper(self):
        #semilla        
        x=randint(0, self.n - 1)
        #factor
        d = 0
        #xi = f(x(i -1))
        xi = x
        #yi = x2i
        yi = (xi**2 + self.a) % self.n
        #Contadores
        i = 0
        j = 1
        #ciclo mas apto para la iteración
        while(True):
            #print(self.a)
            xi = (xi**2 + self.a) % self.n
            #contador de x
            i += 1
            #La funcion y = x2i, por lo tanto x1 -> y2, x2 -> y4, x3 -> y6...xn -> y2n
            while(j < i*2):
                yi = (yi**2 + self.a) % self.n
                #contador de y
                j += 1
            d = gcd(xi-yi, self.n)
            #El ciclo principal while se rompe cuando el factor este entre 1 y N y aparte que sea no trivial (primo).
            #print(d, xi, yi)
            if (d > 1 and d < self.n) and self.Rabin(d) == True:
                break
            #En caso de no encontrar factor, hay que cambiar la semilla y la constante que acompaña a la funcion.
            if xi == (yi % self.n):
                self.a += 1
                #print(self.a)
                self.oper()
        return d
    
    def maxPrims(self):
        list = []
        while True:
            d = int(self.oper())
            self.n = int(self.n / d)
            list.append(d)
            #print(self.n, d)
            if self.Rabin(self.n) == True:
                list.append(self.n)
                break
        return list