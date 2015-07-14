def sum_digits(n):
    return sum(int(x) for x in str(n))

def insertAtPosition(listAfter, x):
    insertMe = 0
    sum_x = sum_digits(x)
    boolCanClose = False
    for i in range (0,len(listAfter)):
        if sum_digits(listAfter[i]) == sum_x:
            insertMe = i+1
            boolCanClose = True
        if listAfter[i] == sum_x+1 and boolCanClose:
            insertMe = i
            break
    if insertMe == 0:
        insertMe = len(listAfter)
    listAfter.insert(insertMe,x)
    return listAfter

listAfter = [1, 10, 2, 11, 3, 4, 5, 6, 7, 8, 9]
x = 12


insertAtPosition(listAfter, x)
print(listAfter)