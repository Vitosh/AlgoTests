def print_matrix(matrix): 
    for i in matrix:
        print(i)
        print

matrix_size = int(input())
matrix_big = []

for i in range(matrix_size):
    small_matrix = list(map(int, input().split()))
    matrix_big.append(small_matrix)

#print_matrix(matrix_big)
for row in range(matrix_size-1,-1,-1):
    for col in range(0, matrix_size):
        if row == matrix_size-1 and col>0:
            matrix_big[row][col] += matrix_big[row][col-1]
        elif row < matrix_size-1 and col>0:            
            down = matrix_big[row+1][col]
            left = matrix_big[row][col-1]
            bigger = down
            if left > down:
                bigger = left
            matrix_big[row][col] += bigger
        
        elif row < matrix_size-1 and col == 0:
            matrix_big[row][col] += matrix_big[row+1][col]
        
print_matrix(matrix_big)
print(matrix_big[0][matrix_size-1])