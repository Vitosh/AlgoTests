str_input = input()
str_goal = input()

def removing_letter(str_goal):
    last_char = str_goal[-1]
    str_goal[:-1]
    if last_char == 'B':
        str_goal = str_goal[::-1]
    return str_goal

while len(str_input) != len(str_goal):
    str_goal = removing_letter(str_input)

if str_input == str_goal:
    print("Possible")	
else:
    print("Impossible")