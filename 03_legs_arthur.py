import heapq

legs = int(input())
legs_length = list(map(int, list(input().split())))
energy = list(map(int, list(input().split())))
usedEnergy = 0

while len(legs_length)>1:

    count_total_legs = len(legs_length)
    firstHighest = sorted(set(legs_length))[-1] 
    firstHighestRepetition = legs_length.count(firstHighest)
    
    if firstHighestRepetition > count_total_legs>>1:
        break
    else:
        remove_at_index = legs_length.index(firstHighest)
        usedEnergy += energy.pop(remove_at_index)
        legs_length.pop(remove_at_index)
        
    
print (usedEnergy)
