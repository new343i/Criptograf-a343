import contfrac
import math    
#Maximo comun divisor
def maximo_comun_divisor(a, b):
    temporal = 0
    while b != 0:
        temporal = b
        b = a % b
        a = temporal
    return a
#Obtener W
def getW(a, b, n):
    list=[]
    for i in range(len(a)):
        p=int(a[i])**2
        q=int(b[i])**2
        w=p-n*q
        list.append(w)
    return list

def congF(a, b, n):
    list=[]
    for i in range(len(a)):
        x=(a[i]**2-b[i])/n
        list.append(x)
    return list
#Congruencia    
def cong(a, n):
    b=1
    x=(a-b)/n
    if a > n:
        while testInt(x) == False:
            b+=1
            x=(a-b)/n
        return b
    elif a <= n:
        return a
#Test de Enteros
def testInt(b):
    bround=round(b)
    terminal=b-bround
    if terminal == 0:
        return True
    else:
        return False

def CFRACv2(find_number):
    lista=[]
    value = (1,math.sqrt(find_number))
    conv = list(contfrac.convergents(value, 10))
    for i in range(len(conv)):
            lista.append(conv[i][1])
    return lista

def CFRACv1(find_number):
    lista=[]
    value = (1,math.sqrt(find_number))
    conv = list(contfrac.convergents(value, 10))
    for i in range(len(conv)):
        lista.append(conv[i][0])
    return lista

listP=[]
listQ=[]
listPCong=[]
listPCongP=[]
listPCongF=[]
listPFCongP=[]
listmcd1=[]
listmcd2=[]
listW = []
listF = []
listF2 = []
listFW = []
listFW2 = []
listWP=[]
listWPF=[]
listWF = []
n =12345
#Obtencion de P y Q
for i in range(len(CFRACv2(n))):
    listP.append(CFRACv2(n)[i])
    listPCong.append(cong(CFRACv2(n)[i], n))
for i in range(len(CFRACv1(n))):
    listQ.append(CFRACv1(n)[i])

#Hacer lista de W
for i in range(len(getW(listP, listQ, n))):
    listW.append(getW(listP, listQ, n)[i])
#print(listW)
#Obtener valores repitidos para hacerlos un cuadrado
for i in range(0, len(listW)):
    if listW.count(listW[i]) >= 2:
        mult =listW.count(listW[i])
        listWP.append(listW[i])
        listPCongP.append(listPCong[i])
#print(listWP, listPCongP)

#Obtener los cuadrados de esos numeros
#for i in range(0, len(listWP), 1):
#    if listWP[i] == listWP[i+1]:
#        listWPF.append(listWP[i]*listWP[i+1]) 
#        listPFCongP.append(listPCongP[i]*listPCongP[i+1])

unique_listWP = []
for i in listWP:
    if i not in unique_listWP:
        unique_listWP.append(i)

for i in range(len(unique_listWP)):
    for j in range(len(listWP)):
        if unique_listWP[i] ==  listWP[j]:
            listF.append(listPCongP[j])
            listF2.append(listWP[j])

def multiplicarLista(l):
    return 0 if len(l)==0 else l[0] if len(l)==1 else l[0]*multiplicarLista(l[1:])

listFP=[]
listFP2=[]
for i in range(int(len(listWP))):
    if i < 4:
        listFP.append(listF2[i])
        listFW.append(listF[i])
    if i > 3:
        listFP2.append(listF2[i])
        listFW2.append(listF[i])

#print(unique_listWP,multiplicarLista(listFW), multiplicarLista(listFW2))


#factorizar los posibles cuadrados y filtrar los que no lo son
for i in range(len(listW)):
    if listW[i] < 0:
        if testInt(math.sqrt(-listW[i])) == True:
            listWF.append(-math.sqrt(-listW[i]))
            listPCongF.append(listPCong[i])
    else:
        if testInt(math.sqrt(listW[i])) == True and listW[i] != 1:
            listWF.append(math.sqrt(listW[i]))
            listPCongF.append(listPCong[i])
#print(listWF)
#print(listPCongF)
#sumar los valores repetidos
for i in range(len(listWPF)):
    listWF.append(math.sqrt(listWPF[i]))
    listPCongF.append(listPFCongP[i])

for i in range(len(unique_listWP)):
    listWF.append(unique_listWP[i])
if multiplicarLista(listFW) != 0:
    listPCongF.append(multiplicarLista(listFW))
if multiplicarLista(listFW2) != 0:
    listPCongF.append(multiplicarLista(listFW2))

#print(listWF)
#print(listPCongF)

#Factores obtenidos con valores combinados de W
listWFComb = []
listPCongFComb = []
for i in range(int(len(listFP))):
    for j in range(int(len(listFP2))):
        listPCongFComb.append(listFP[i]*listFP2[j])
        listWFComb.append(listFW[i]*listFW2[j])
#print(listFP, listFP2, listPCongFComb, listWFComb)
      
#Factores obtenidos con valores de W solos
for i in range(len(listPCongF)):
    if testInt(maximo_comun_divisor(n, listPCongF[i]-listWF[i])) == True:
        listmcd1.append(maximo_comun_divisor(n, listPCongF[i]-listWF[i]))
    if testInt(maximo_comun_divisor(n, listPCongF[i]+listWF[i])) == True:
        listmcd2.append(maximo_comun_divisor(n, listPCongF[i]+listWF[i]))

for i in range(len(listPCongFComb)):
    if testInt(maximo_comun_divisor(n, listPCongFComb[i]-listWFComb[i])) == True:
        listmcd1.append(maximo_comun_divisor(n, listPCongFComb[i]-listWFComb[i]))
    if testInt(maximo_comun_divisor(n, listPCongFComb[i]+listWFComb[i])) == True:
        listmcd2.append(maximo_comun_divisor(n, listPCongFComb[i]+listWFComb[i]))

listmcd1F = []
listmcd2F = []
for i in range(len(listmcd1)):
    if listmcd1[i] and listmcd2[i] != 1:
        listmcd1F.append(listmcd1[i])
        listmcd2F.append(listmcd2[i])

#print(listWFComb, '\n',listPCongFComb, '\n')
FactoresFinalmenteFinal = dict(zip(listmcd1, listmcd2))
print(listmcd1, listmcd2)
print(FactoresFinalmenteFinal)


