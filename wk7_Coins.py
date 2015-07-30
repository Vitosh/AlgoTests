target_sum = 26
coins = [1,2,5,10,20,50, 100]
coin_count = 7
i = 0

def count_me(i,coins,coin_count,target_sum):
    i += 1
    print(i)
    if (target_sum) == 0:
        return 1
    if (target_sum < 0) or (coin_count<= 0):
        return 0
    return count_me(i,coins,coin_count-1, target_sum) + count_me(i,coins, coin_count, target_sum-coins[coin_count-1])

print(count_me(i,coins, coin_count, target_sum))

