sentence = list(input().split())
#print(sentence)
result = ''
for word in sentence:
    s_word = ''
    s_word = "".join(word)
    s_word = s_word.capitalize()
    result += s_word + " "
    
print(result[:-1])