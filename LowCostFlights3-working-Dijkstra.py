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
list_total_results = []
int_total_numbers_count = int(input())
list_matrix = []

for i in range(0, int_total_numbers_count):
    list_matrix.append(list(map(int, input().split())))

tasks_to_calculate = int(input())
tasks = []

for i in range(0, tasks_to_calculate):
    tasks.append(list(map(int, input().split())))
#End of the input

for k in range (0, int_total_numbers_count):
    list_results = []
    list_visited = []
    
    list_results = [float('inf')]  * int_total_numbers_count
    list_visited = [0] * int_total_numbers_count 
    list_results[k] = 0
    
    while(sum(list_visited) != sum(1 for z in list_results if z < float('inf') )):
        
        visiting_currently = visit_position(list_results, list_visited)
        #print(visiting_currently)
        current_value = list_results[visiting_currently]
        #setting the value of visited
        list_visited[visiting_currently] = 1
        
        for i in range(0, int_total_numbers_count):
            if list_matrix[visiting_currently][i] != 0 and list_matrix[visiting_currently][i]  + current_value < list_results[i]:
                list_results[i] = list_matrix[visiting_currently][i] + current_value
         
    list_total_results.append(list_results)

for small_task in tasks:
    fly_from = small_task[0]
    fly_to = small_task[1]
    printed_value = list_total_results[fly_from][fly_to]
    if printed_value == float('inf'):
        print('NO WAY')
    else:
        print(printed_value)