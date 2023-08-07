import contfrac
import math
class CFRACMethod:
    
    def __init__(self, n):
        self.n=n

    def maximo_comun_divisor(self, a, b):
        temporal = 0
        while b != 0:
            temporal = b
            b = a % b
            a = temporal
        return a

    def getW(self, a, b, n):
        list=[]
        for i in range(len(a)):
            p=int(a[i])**2
            q=int(b[i])**2
            w=p-n*q
            list.append(w)
        return list

    def congF(self, a, b, n):
        list=[]
        for i in range(len(a)):
            x=(a[i]**2-b[i])/n
            list.append(x)
        return list
        
    def cong(self, a, n):
        b=1
        x=(a-b)/n
        if a > n:
            while self.testInt(x) == False:
                b+=1
                x=(a-b)/n
            return b
        elif a <= n:
            return a

    def testInt(self, b):
        bround=round(b)
        terminal=b-bround
        if terminal == 0:
            return True
        else:
            return False

    def CFRACv2(self, find_number):
        lista=[]
        value = (1,math.sqrt(find_number))
        conv = list(contfrac.convergents(value, 100000))
        for i in range(len(conv)):
                lista.append(conv[i][1])
        return lista

    def CFRACv1(self, find_number):
        lista=[]
        value = (1,math.sqrt(find_number))
        conv = list(contfrac.convergents(value, 100000))
        for i in range(len(conv)):
            lista.append(conv[i][0])
        return lista

#P2-N*Q2