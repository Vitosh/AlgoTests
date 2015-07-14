listInput = input().split()
intSoldiers = int(listInput[0])
intRows = int(listInput[1])
listSoldiers = []


for i in range(0,intRows):
    listLine = []
    listLine = input().split()
    listLine = [int(i) for i in listLine]
    listSoldiers.append(listLine)
listResults = []


def Calculate():
    intMaxJumps = ((intSoldiers-1)*intSoldiers)/2    
    #print("max => {}".format(intMaxJumps) )
    for i in range(0, intRows):
        intResultRow = 0
        
        for z in range(0, intSoldiers):
            #print(listSoldiers[i][z])
            for otherSoldiers in range(z, intSoldiers):
                
                if listSoldiers[i][z]<listSoldiers[i][otherSoldiers]:
                    intResultRow += 1
                    #print("{} jumps for {} from column {}".format(listSoldiers[i][z],listSoldiers[i][otherSoldiers],i))
                    
                    if intResultRow == 0:
                        return(i)
    
        listResults.append(intResultRow)
    intMaxJumps = min(listResults)
    return listResults.index(intMaxJumps)
        
result = Calculate()
print(result+1)