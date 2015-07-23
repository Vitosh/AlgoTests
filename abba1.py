input_word = input()
input_target = input()

def a_to_end(input_word):
    return input_word + 'A'

def b_to_end(input_word):
    input_word = input_word[::-1]
    return input_word + 'B'

