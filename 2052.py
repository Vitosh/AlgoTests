intNumber = int(input())+1
listNew = [x  for x in range(1,intNumber)]
listAfter = [1,2]

for x in range(3,intNumber):
    insertMe = 0
    sum_x = sum(map(int,str(x)))
    boolCanClose = False
    
    for i in range (0,len(listAfter)):
        if sum(map(int,str(listAfter[i]))) == sum_x:
            insertMe = i+1
            boolCanClose = True
        if listAfter[i] == sum_x+1 and boolCanClose:
            insertMe = i
            break
    if insertMe == 0:
        insertMe = len(listAfter)
    listAfter.insert(insertMe,x)    

listFinal = zip(listAfter,listNew)
intResult = 0

for k in listFinal:
    if k[0] == k[1]:
        intResult += 1
print(intResult)