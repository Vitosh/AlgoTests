target = 11
coins = [1,2,5,10]
my_array = [0]*(target+1)

for coin in coins:
    for i in range(target+1):
        if coin == i:
            my_array[i]+=1
        if i-coin>0:
            my_array[i]=((my_array)[i]+my_array[i-coin])
print(my_array)
print(my_array[target])