intDonaldHeroes = int(input())
listDonald=[]

listA = ['A','P','O','R']
listB = ['B','M','S']
listC = ['D','G','J','K','T','W']

def calculateSteps(sCurrent, sNext):
    if (sCurrent in listA) and (sNext in listA):
        return 0
    elif (sCurrent in listB) and (sNext in listB):
        return 0
    elif (sCurrent in listC) and (sNext in listC):
        return 0
    elif (sCurrent in listB) or (sNext in listB):
        return 1
    else:
        return 2

for x in range (0, intDonaldHeroes):
    strFirst = input()
    listDonald.append(strFirst[:1])

intResult = 0
if listDonald[0] in listB:
    intResult = 1
elif listDonald[0] in listC:
    intResult = 2

for x in range (0, len(listDonald)-1):
    sCurrent = listDonald[x]
    sNext = listDonald[x+1]
    intResult += calculateSteps(sCurrent, sNext)

print(intResult)