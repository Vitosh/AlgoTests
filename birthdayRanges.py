listFirstLine = list(input().split())
listSecondLine = list(input().split())
    
listFirstLine = list(map(int, listFirstLine))
listSecondLine = list(map(int, listSecondLine))

listSecondLine.sort()
listRanges = []
iRangesCount = listFirstLine[1]

for i in range(0,iRangesCount):

    line = list(input().split())
    line = list(map(int, line))    
    listRanges.append(line)
newList = [0]*367

for i in listSecondLine:
    newList[i+1] +=1
#print(listSecondLine)
#print(newList)
anotherNewList = [0] *367
for i in range(1,367):
    anotherNewList[i] = anotherNewList[i-1]+newList[i]

#print(anotherNewList)

for list in listRanges:
    smaller = list[0]
    bigger = list[1]
    print(anotherNewList[bigger+1]-anotherNewList[smaller])