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

def print_matrix(matrix):
    for i in matrix:
        print(i)
        print
        
#Start of the input
number_of_tests = int(input())
for case in range(number_of_tests):
    number_of_nodes = int(input())
    list_matrix = []
    
    for i in range(number_of_nodes-1):
        list_matrix.append(list(map(int, input().split())))
#End of the input
    list_addresses = [[float('inf') for i in range (number_of_nodes)] for j in range(number_of_nodes)]
    for i in range(number_of_nodes-1):
        from_node = list_matrix[i][0]
        to_node = list_matrix[i][1]
        node_value = list_matrix[i][2]
        
        list_addresses[from_node][to_node] = node_value
        list_addresses[to_node][from_node] = node_value
    

    #print_matrix(list_addresses)
    list_total_results = []

    for k in range(number_of_nodes):
        list_results = []
        list_visited = []
        
        list_results = [float('inf')]  * number_of_nodes
        list_visited = [0] * number_of_nodes 
        list_results[k] = 0
        
        while(sum(list_visited) != sum(1 for z in list_results if z < float('inf') )):
        
            visiting_currently = visit_position(list_results, list_visited)
            current_value = list_results[visiting_currently]
            list_visited[visiting_currently] = 1
        
            for i in range(0, number_of_nodes):
                if list_addresses[visiting_currently][i] != 0 and list_addresses[visiting_currently][i]  + current_value < list_results[i]:
                    list_results[i] = list_addresses[visiting_currently][i] + current_value
        
        list_total_results.append(list_results)     
            
    #print_matrix(list_total_results)
    avg_value = 0
    counter = 0
    sum_values = 0
    for matrix in list_total_results:
        for number in matrix:
            if number != 0:
                counter += 1
                sum_values += number
                
    print(sum_values/counter)
                
        
        
        
        
    
    
    
    