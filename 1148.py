strFirstLine = input()
listFirstLine = strFirstLine.split()

intBricks = int(listFirstLine[0])
intLevels = int(listFirstLine[1])
intStarting = int(listFirstLine[2])
listInputData = []
listOfList = []

while True:
    intData = int(input())
    if intData < 0:
        break
    listInputData.append(intData)

while True:
    intBricksUsed = 0
    result = []
    result[0] = intStarting
    for x in range(1, intLevels):
        result[x]
        
        
        