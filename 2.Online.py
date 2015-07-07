import math
def calculateMedian(myList):
    myList.sort()
    all = len(myList)-1
    
    return myList[math.ceil(all/2)]

def calculate(txtInput):
    myList = []
    for i in txtInput:
        myList.append(i)
        result = calculateMedian(myList)
        print(result)

def main():
    i = int(input())
    txtInput = list(input().split())
    myList = map(int, txtInput )
    calculate(myList)
main()