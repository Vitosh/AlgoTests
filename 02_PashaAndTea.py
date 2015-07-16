friends_and_teapotsize = list(map(int, list(input().split())))
cup_size = list(map(int, list(input().split())))

total_boys = friends_and_teapotsize[0]
total_teapot = friends_and_teapotsize[1]
cup_size.sort(reverse=False)
smallest_girl_cup = cup_size[0]
smallest_boy_cup = cup_size[total_boys]

tea_per_girl = 0

if smallest_girl_cup*2 < smallest_boy_cup:
    smallest_boy_cup = smallest_girl_cup*2
    
if smallest_girl_cup*2 > smallest_boy_cup:
    smallest_girl_cup = smallest_boy_cup/2

max_tea_per_girl = total_teapot/(3*total_boys)

if max_tea_per_girl > smallest_girl_cup:
    max_tea_per_girl = smallest_girl_cup

if max_tea_per_girl > smallest_boy_cup/2:
    max_tea_per_girl = smallest_boy_cup/2

result = max_tea_per_girl * total_boys * 3
print(result)