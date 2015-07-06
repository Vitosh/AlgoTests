listFirstLine = list(input().split())
d = {}
for i in range(0, int(listFirstLine[0])):
    myList = list(input().split())
    d[int(myList[0])] = myList[1]

newList = []
for i in range(0, int(listFirstLine[1])):
    newList.append(int(input()))
    
for i in newList:
    print(d[i])
