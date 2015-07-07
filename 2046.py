def strBuilder(lstLine):
    strLine = "|"
    for z in range (0,len(lstLine)):
        strLine += str(lstLine[z])
        strLine += " " *(intMagicNumber-len(lstLine[z])) + "|"
    return strLine
    
def listSplitMe(strText):
    listText = strText.split()
    strWrite = ""
    lastLine = ""
    
    for i in range(0,len(listText)):
        if len(lastLine)+ len(listText[i])>9:
            strWrite+=lastLine+"\n"
            lastLine = listText[i]
            if i == len(listText)-1:
                strWrite+=lastLine
        else:
            if i == 0:
                lastLine+=listText[i]
            else:
                lastLine+=" " + listText[i]
            if i == len(listText)-1:
                strWrite+=lastLine
            
    return strWrite.split(sep="\n")


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
            listLinesUsed.append(len(listSplitMe(strSubject)))
        else:
            listLinesUsed.append(1)
            
listLinesUsedRebuild = []
    

for row in range (0,12,3):
    intMaxLines= max(listLinesUsed[row+0] , listLinesUsed[row+1] , listLinesUsed[row+2])
    listLinesUsedRebuild.append(intMaxLines)
#print(listLinesUsedRebuild)

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
        listMain = []
        for column in range(1,4):
            listTest = []
            listNew = []
            
            listTest.append(row)
            listTest.append(column)
            if listTest in listPosition:
                strSubject = listSubjectName[listPosition.index(listTest)]
                listNew.extend(listSplitMe(strSubject))

            if ((int(listLinesUsedRebuild[row-1]))>len(listNew)):
                intDifference = int(listLinesUsedRebuild[row-1])-len(listNew)
                listAdditional = ["" for a in range(intDifference)]
                listNew.extend(listAdditional)
                
            listMain.append(listNew)                                   
        
        #print(listMain)
        listNewMain = []
        for a in range(0, len(listNew)):
            listSubList = []            
            for b in range(0, len(listMain)):
                listSubList.append(listMain[b][a])
            listNewMain.append(listSubList)
            
        #print(listNewMain)
        for li in listNewMain:
            print(strBuilder(li))
print(strLineBluePrint)