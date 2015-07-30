#https://arena.topcoder.com/#/u/practiceCode/16527/48824/13917/2/326683
#tests with results, uncomment for input:

#jecjxsengslsmeijrmcx
#tcfyhumjcvgkafhhffed
#icmgxrlalmhnwwdhqerc
#xzrhzbgjgabanfxgabed
#fpcooilmwqixfagfojjq
#xzrzztidmchxrvrsszii
#swnwnrchxujxsknuqdkg
#rnvzvcxrukeidojlakcy
#kbagitjdrxawtnykrivw
#towgkjctgelhpomvywyb
#ucgqrhqntqvncargnhhv
#mhvwsgvfqgfxktzobetn
#fabxcmzbbyblxxmjcaib
#wpiwnrdqdixharhjeqwt
#xfgulejzvfgvkkuyngdn
#kedsalkounuaudmyqggb
#gvleogefcsxfkyiraabn
#tssjsmhzozbcsqqbebqw
#ksbfjoirwlmnoyyqpbvm
#phzsdodppzfjjmzocnge
#376

#helloand
#welcomet
#osingler
#oundmatc
#hsixhund
#redandsi
#xtythree
#goodluck
#56

#zz
#zz
#2

input_word = input()
matrix = []
matrix.append(list(input_word))

for i in range(0, len(input_word)-1):
    matrix.append(list(input()))

dict_1 = {}
dict_2 = {}

for i in range (0, len(matrix)):
    for k in range(0, len(matrix)):
        char_to_add = matrix[i][k]
        if (i%2 == 1 and k%2 == 1) or (i%2 == 0 and k%2 == 0):
            if char_to_add in dict_1:
                dict_1[char_to_add] += 1
            else:
                dict_1[char_to_add] = 1
        else:
            if char_to_add in dict_2:
                dict_2[char_to_add] += 1
            else:
                dict_2[char_to_add] = 1            

print(dict_1)
print(dict_2)

dict_1_highest = max(dict_1, key=dict_1.get)
dict_2_highest = max(dict_2, key=dict_2.get)

print(dict_1_highest)
print(dict_2_highest)

dict_1_highest_repetition = dict_1[dict_1_highest]
dict_2_highest_repetition = dict_2[dict_2_highest]

print(dict_1_highest_repetition)
print(dict_2_highest_repetition)
print(len(matrix)*2)

#check if we have a problem here:
if dict_1_highest == dict_2_highest:
    dict_1[dict_1_highest] = 0
    dict_2[dict_2_highest] = 0

    dict_1_highest = max(dict_1, key=dict_1.get)
    dict_2_highest = max(dict_2, key=dict_2.get)
    
    dict_1_highest_repetition_2 = dict_1[dict_1_highest]
    dict_2_highest_repetition_2 = dict_2[dict_2_highest]   
    
    if dict_1_highest_repetition_2>dict_2_highest_repetition_2:
        dict_3_highest = dict_1_highest_repetition_2
    else:
        dict_3_highest = dict_2_highest_repetition_2
    
    result = len(matrix)**2 - dict_1_highest_repetition - dict_3_highest
else:
    result = len(matrix)**2 - dict_1_highest_repetition - dict_2_highest_repetition

print(result)


