from iteration_utilities import *
from functools import reduce
listWP=[13, 13]
listPCongP=[502, 535]
list1 = [13, 13]
list2 = [502, 535]
listF = []
listF2 = []
listFW = []
listFW2 = []

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

for i in range(int(len(listWP))):
    if i < 4:
        listFW.append(listF[i])
    if i > 3:
        listFW2.append(listF[i])

print(listFW, listFW2, unique_listWP)
print(multiplicarLista(listFW), multiplicarLista(listFW2))
#print(listF, listF2)