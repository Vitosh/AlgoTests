import shlex

string_input = input()
string_input = string_input.replace("{", "")
string_input = string_input.replace("}", "")

list_string_input = list(string_input.split(","))
matrix = []

for e in list_string_input:
    k = list(e)
    empty_list = []
    for e in k:
        if e != chr(34)  and e != chr(39) and e != chr(32):
            empty_list.append(e)
    matrix.append(empty_list)
                
print(matrix)

count_first = 0
count_second = 0
dict_first = {}
dict_second = {}

first_line = False

for i in range(0, len(matrix)):
    first_line = not first_line
    for k in range(0, len(matrix)):
        if (first_line and k%2 == 0) or (not first_line and k%2 == 1):
            if matrix[i][k] in dict_first:
                dict_first[matrix[i][k]] += 1
            else:
                dict_first[matrix[i][k]] = 1
        else:
            if matrix[i][k] in dict_second:
                dict_second[matrix[i][k]] += 1
            else:
                dict_second[matrix[i][k]] = 1 

#print(dict_first)
#print(dict_second)

max_first_value = max(dict_first, key=dict_first.get)
max_second_value = max(dict_second, key=dict_second.get)
a = max_first_value
b = max_second_value
print(a)

print(aa)
print(bb)
aa = dict_first[max_first_value]
bb = dict_second[max_second_value]
print((len(matrix))*2-aa-bb)

if max_first_value == max_second_value:
    dict_first[max_first_value] = 0
    dict_second[max_second_value] = 0
    
    max_first_value2 = max(dict_first, key=dict_first.get)
    max_second_value2 = max(dict_second, key=dict_second.get)
    
    if max_first_value2>max_second_value2:
        max_third = max_first_value2
    else:
        max_third = max_second_value2
        
    print(len(matrix)*2-a-max_third)