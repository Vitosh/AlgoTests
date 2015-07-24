def calculate_in_matrix(columns, lines, word, word_reversed, list_matrix):
    current_result = 0
    
    difference_in_lines = columns - len(word) + 1
    if difference_in_lines:
        for i in range (0, lines):
            for k in range (0, difference_in_lines):
                
                test_result = list_matrix[i]    
                test_result = "".join(test_result[k:k+len(word_as_list)])
                        
                if test_result == word or test_result == word_reversed:
                    current_result += 1
    return current_result


def mirror_matrix(list_matrix):
    reversed_matrix = []
    for line in list_matrix:
        
        reversed_matrix.append(line[::-1])
    return reversed_matrix


def calculate_in_diagonals(columns, lines, word, word_reversed, list_matrix):
    current_result = 0
    difference_in_lines = lines - word_size + 1
    difference_in_columns = columns - word_size + 1
    
    for p in range(0, difference_in_columns):
        matrix = [row[p:] for row in list_matrix]
        for i in range(0, difference_in_lines):
            diagonal_word = ""        
            for m in range(0+i, word_size+i):
                for k in range(0,word_size):
                    if m-i == k:
                        diagonal_word += matrix[m][k]
                        if diagonal_word == word or diagonal_word == word_reversed:
                            current_result += 1
    return current_result


word = input()
word_size = len(word)
word_reversed = word[::-1]
word_as_list = list(word)

size_matrix = list(map(int, input().split()))
lines = size_matrix[0]
columns = size_matrix[1]

list_matrix = []

for i in range(0, lines):
    list_matrix.append(list(input().split()))

result = 0
#check horizontal lines >>>>
result += calculate_in_matrix(columns,lines, word, word_reversed, list_matrix)
#reversing matrix
list_matrix_reversed = [[list_matrix[j][i] for j in range(len(list_matrix))] for i in range(len(list_matrix[0]))]
#check vertical lines vvvv
result += calculate_in_matrix(lines, columns, word, word_reversed, list_matrix_reversed)
result += calculate_in_diagonals(columns, lines, word, word_reversed, list_matrix)

list_matrix = mirror_matrix(list_matrix)

result += calculate_in_diagonals(columns, lines, word, word_reversed, list_matrix)
print(result)