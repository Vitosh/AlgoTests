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
starting_point = list_first_line[2]
ending_point = list_first_line[3]

list_addresses = []

for i in range(0, roads):
    list_addresses.append(list(map(int, input().split())))
    
list_matrix = [[float('inf') for i in range (crosses)] for j in range(crosses)]
list_total_results = []
#End of the input

for i in range(0, (roads)):
    from_street = list_addresses[i][0]-1    
    to_street = list_addresses[i][1] -1
    value_street = list_addresses[i][2]
    
    list_matrix[from_street][to_street] = value_street
    list_matrix[to_street][from_street] = value_street
print(list_matrix)
matrix_visited_peaks = []

for k in range (0, crosses):
    list_results = []
    list_visited = []
    
    list_results = [float('inf')]  * crosses
    list_visited = [0] * crosses 
    list_results[k] = 0
    matrix_visited_peaks.append
    while(sum(list_visited) != sum(1 for z in list_results if z < float('inf') )):
        visiting_currently = visit_position(list_results, list_visited)
        
        # print(visiting_currently)
        current_value = list_results[visiting_currently]
        # setting the value of visited
        list_visited[visiting_currently] = 1

        for i in range(0, crosses):
            if list_matrix[visiting_currently][i] != 0 and list_matrix[visiting_currently][i]  + current_value < list_results[i]:
                list_results[i] = list_matrix[visiting_currently][i] + current_value     
    list_total_results.append(list_results)
    
for i in range(0, len(list_total_results)):
    print (list_total_results[i])  
