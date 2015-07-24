def visit_position(list_results,list_visited):
    #returns the position in list_results of the smallest value, which is not visited
    
    list_smallest = []
    smallest_value = float('inf')
    
    for i in range(0,len(list_visited)):       
        if list_results[i] != float('inf') and list_visited[i] == 0:
            list_smallest.append(i)
            
    for i in range(0, len(list_smallest)):
        
        if list_results[list_smallest[i]]<smallest_value:
            smallest_value = list_results[list_smallest[i]]
            smallest_position = list_smallest[i]

    return smallest_position

#Start of the input
list_first_line = list(map(int, input().split()))

crosses = list_first_line[0]
roads = list_first_line[1]
starting_point = list_first_line[2]-1
ending_point = list_first_line[3]-1

list_addresses = []

for i in range(0, roads):
    list_addresses.append(list(map(int, input().split())))
    
list_matrix = [[float('inf') for i in range (crosses)] for j in range(crosses)]
list_total_results = []
list_total_coming_from = [0] * crosses
#End of the input

for i in range(0, (roads)):
    from_street = list_addresses[i][0]-1    
    to_street = list_addresses[i][1] -1
    value_street = list_addresses[i][2]
    
    list_matrix[from_street][to_street] = value_street
    list_matrix[to_street][from_street] = value_street

matrix_visited_peaks = []

list_results = []
list_visited = []

list_results = [float('inf')]  * crosses
list_visited = [0] * crosses 
list_results[starting_point] = 0

#visiting currently is set to -1, in order to be different from the ending point
visiting_currently = -1
list_total_coming_from[starting_point] = -1

while visiting_currently != ending_point:
    visiting_currently = visit_position(list_results, list_visited)
    current_value = list_results[visiting_currently]
    list_visited[visiting_currently] = 1
    
    for i in range(0, crosses):
        if list_matrix[visiting_currently][i] != 0 and list_matrix[visiting_currently][i]  + current_value < list_results[i]:
            list_results[i] = list_matrix[visiting_currently][i] + current_value     
            last_updated_value = i
            list_total_coming_from[last_updated_value]= visiting_currently+1
print(list_total_coming_from)
print(list_results[ending_point])
list_total_results.extend(list_results)

start_from = ending_point

result_to_display = []
result_to_display.append(ending_point+1)
# we need -2, because we finish at -1 and we remove 1 from the answer (-1-1=-2)
while(start_from != -2):
    start_from = list_total_coming_from[start_from]-1
    if start_from != -2:
        result_to_display.append(start_from+1)

print(result_to_display[::-1]) #cheap reversing in python :)