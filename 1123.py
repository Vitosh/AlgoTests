def listToInt(myList):
    myInt = int(''.join(myList))
    return myInt

def intToList(myInt):
    strInt = str(myInt)
    myList = list(strInt)
    return myList


def calculate(strInput):
    if (len(strInput) == 1):
        return int(strInput)
    
    intOldSalary = int(strInput)
    listNum = list(strInput)
    
    listHalf1 = list(listNum[:int(len(listNum)/2)])
    listHalf2 = list(listNum[int(len(listNum)/2):])
    boolHasEdge = bool(len(listNum)%2 != 0)
    
    if boolHasEdge:
        strEdge = listHalf2.pop(0)
    
    if listToInt(listHalf2)> int(str(listToInt(listHalf1))[::-1]):
        if boolHasEdge:
            if strEdge != "9":
                strEdge = str(int(strEdge)+1)
                strTempList = str(listToInt(listHalf1))
            else:
                strEdge = "0"
                intTempList = listToInt(listHalf1)
                intTempList += 1
                strTempList = str(intTempList)
            intResult = int(strTempList+strEdge+strTempList[::-1])
        else:
            strTempList = str(listToInt(listHalf1)+1)
            intResult = int(strTempList+strTempList[::-1])
    else:
        if boolHasEdge:
            intResult = int(str(listToInt(listHalf1)) + strEdge + str(listToInt(listHalf1))[::-1])
        else:
            intResult = int(str(listToInt(listHalf1)) + str(listToInt(listHalf1))[::-1])
    
    return intResult

strInput = input()
print(calculate(strInput))
