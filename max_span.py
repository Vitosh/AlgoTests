number = int(input())
number_list = list(map(int, input().split()))

result = 0

for i in range(0, number):
    for z in range(i, number):
        current_number = number_list[i]
        if number_list[z] == number_list[i]:
            if result < z-i+1:
                result = z-i+1

print(result)