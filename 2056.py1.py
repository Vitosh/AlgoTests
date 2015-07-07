intSubjectsCount = int(input())
listGrades = []
listGrades.sort()

for x in range(0, intSubjectsCount):
    listGrades.append(int(input()))

if 3 in listGrades:
    print("None")
    
elif sum(listGrades)/intSubjectsCount == 5:
    print("Named")

elif sum(listGrades)/intSubjectsCount >=4.5:
    print("High")
    
else:
    print("Common")
