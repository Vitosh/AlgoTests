def visit_position(list_results,list_visited):
    #returns the position in list_results of the smallest value, which is not visited
    print(list_results,list_visited)
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

def up_left_exists(matrix,row,col):
    if row == 0 or col == 0:
        return False
    else:
        return True

def up_right_exists(matrix,row,col):
    if row == 0 or col == matrix_size-1:
        return False
    else:
        return True

def up_middle_exists(matrix,row,col):
    if row > 0:
        return True
    else:
        return False    

def same_line_left_exists(matrix,row,col):
    if col>0:
        return True
    else:
        return False

def value_position(matrix,row,col):
    result = len(matrix)*row + col
    return(result)

#start of the input
matrix_size = int(input())
matrix_doubled_size = matrix_size ** 2
first_line = list(map(int, input().split()))

list_addresses = []
for i in range(0, matrix_size):
    list_addresses.append(list(map(int, input().split())))

real_matrix = []
for k in range(0, matrix_size**2):
    list_temp = [float('inf')] * matrix_size**2
    real_matrix.append(list_temp)

for k in range(0, matrix_size):
    for p in range(0, matrix_size):
        current_value = list_addresses[k][p]
        position_current = value_position(list_addresses,k,p)
        
        if up_left_exists(list_addresses, k, p):                
            value_to_assign = abs(list_addresses[k-1][p-1]-current_value)+1
                        
            position_target = value_position(list_addresses,k-1,p-1)
            
            real_matrix[position_current][position_target] = value_to_assign
            real_matrix[position_target][position_current] = value_to_assign
            
        if up_right_exists(list_addresses, k, p):    
            value_to_assign = abs(list_addresses[k-1][p+1]-current_value)+1
            
            position_target = value_position(list_addresses,k-1,p+1)
            
            real_matrix[position_current][position_target] = value_to_assign
            real_matrix[position_target][position_current] = value_to_assign
            
        if up_middle_exists(list_addresses, k, p):
            value_to_assign = abs(list_addresses[k-1][p]-current_value)+1
            
            position_target = value_position(list_addresses,k-1,p)
        
            real_matrix[position_current][position_target] = value_to_assign
            real_matrix[position_target][position_current] = value_to_assign
        
        if same_line_left_exists(list_addresses, k, p):
            value_to_assign = abs(list_addresses[k][p-1]-current_value)+1
            
            position_target = value_position(list_addresses,k,p-1)
            
            real_matrix[position_current][position_target] = value_to_assign
            real_matrix[position_target][position_current] = value_to_assign    

#here comes the boom:
print_matrix(real_matrix)

starting_point = value_position(list_addresses,first_line[0],first_line[1])
ending_point = value_position(list_addresses,first_line[2],first_line[3])
list_total_results = []

for y in range(0, matrix_doubled_size):
    list_results = [float('inf')] * (matrix_size*matrix_size)
    list_visited = [0] * (matrix_size*matrix_size)
    list_results[y] = 0 #from starting point to starting point is 0
    
    while (sum(list_visited) != sum(1 for z in list_results if z < float('inf'))):
        visiting_currently = visit_position(list_results, list_visited)
        current_value = list_results[visiting_currently]
        list_visited[visiting_currently] = 1
        
        for i in range(0, matrix_doubled_size):
            if real_matrix[visiting_currently][i] != 0 and real_matrix[visiting_currently][i]+current_value< list_results[i]:
                list_results[i] = real_matrix[visiting_currently][i] + current_value
    list_total_results.append(list_results)
            
print_matrix(list_total_results)   
print("The required results is:")
print(list_total_results[starting_point][ending_point])