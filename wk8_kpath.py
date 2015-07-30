def print_matrix(matrix): 
    for i in matrix:
        print(i)
        print

matrix_size = int(input())
matrix_big = [[float('inf') for i in range (matrix_size)] for j in range(matrix_size)]

for i in range(matrix_size-1):
    small_matrix = list(map(int, input().split()))
    matrix_big[small_matrix[0]][small_matrix[1]] = small_matrix[1]
    matrix_big[small_matrix[1]][small_matrix[0]] = small_matrix[0]    

task = list(map(int, input().split()))
print_matrix(matrix_big)