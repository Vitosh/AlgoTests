intSubjectsCount = int(input())
listSubjectName = []
listPosition = []

for x in range(0, intSubjectsCount):
    listSubjectName.append(input())
    lstSecondtLine = input()
    lstSecondtLine = lstSecondtLine.replace("Tuesday","1")
    lstSecondtLine = lstSecondtLine.replace("Thursday","2")
    lstSecondtLine = lstSecondtLine.replace("Saturday","3")
    listSecondLine = lstSecondtLine.split()
    listSecondLine[0], listSecondLine[1] = listSecondLine[1], listSecondLine[0] 
    listSecondLine = list(map(int,listSecondLine))
    listPosition.append(listSecondLine)

strLineBluePrint = "+----------+----------+----------+"

intMagicNumber = 10

listLinesUsed = []
for row in range(1,5):
    for column in range(1,4):
        listTest = []
        listTest.append(row)
        listTest.append(column)
        
        if listTest in listPosition:
            strSubject = listSubjectName[listPosition.index(listTest)]
            intLen = len(strSubject)
            if intLen>10:
                listLinesUsed.append(2)
            else:
                listLinesUsed.append(1)
        else:
            listLinesUsed.append(1)
            
listLinesUsedRebuild = []

def strBuilder(lstLine):
    strLine = "|"
    for z in range (0,3):
        strLine += str(lstLine[z])
        strLine += " " *(intMagicNumber-len(lstLine[z])) + "|"
    return strLine
    
    

for row in range (0,12,3):
    intSum = listLinesUsed[row+0] + listLinesUsed[row+1] + listLinesUsed[row+2]
    if intSum>3:
        listLinesUsedRebuild.append(2)
    else:
        listLinesUsedRebuild.append(1)

for row in range(1,5):
    print(strLineBluePrint)
    if listLinesUsedRebuild[row-1]<2:
        strLine = "|"
        for column in range(1,4):
            listTest = []
            listTest.append(row)
            listTest.append(column)
            if listTest in listPosition:
                strSubject = listSubjectName[listPosition.index(listTest)]
                intLen = len(strSubject)
                strLine += (strSubject)
                strLine += " "* (intMagicNumber-intLen) +"|"
                
            else:
                strLine += " "*intMagicNumber +"|"
        print(strLine)
    else:
        lstFirstLine = []
        lstSecondtLine = []
        for column in range(1,4):
            listTest = []
            listTest.append(row)
            listTest.append(column)
            if listTest in listPosition:
                strSubject = listSubjectName[listPosition.index(listTest)]
                intLen = len(strSubject)
                if intLen > 10:
                    listSubject = list(strSubject.split())
                    lstFirstLine.append(listSubject[0])
                    lstSecondtLine.append(listSubject[1])
                else:
                    lstFirstLine.append(strSubject)
                    lstSecondtLine.append("")                    
            else:
                lstFirstLine.append("")
                lstSecondtLine.append("")
        
        print(strBuilder(lstFirstLine))
        print(strBuilder(lstSecondtLine))
            
        
print(strLineBluePrint)