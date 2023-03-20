class PollardsMethod:
    def maximo_comun_divisor(self, a, b):
        temporal = 0
        while b != 0:
            temporal = b
            b = a % b
            a = temporal
        return a
    def testInt(self, b):
        bround=round(b)
        terminal=b-bround
        if terminal == 0:
            return True
        else:
            return False

    def oper(self, n):
        x=2
        xi=[]
        yi=[]
        resul=[]
        resul1=[]
        for i in range(0, 20):
            x=x**2+1
            xi.append(x)
        for j in range(1, 20, 2):
            y=xi[j]
            yi.append(y)
        for k in range(len(yi)):
            resul.append(self.maximo_comun_divisor(xi[k]-yi[k], n))
        for r in range(len(resul)):
            if resul[r] != 1:
                resul1.append(resul[r])
        if bool(resul1) == False:
            return 0
        #print(resul1)
        return resul1[0]