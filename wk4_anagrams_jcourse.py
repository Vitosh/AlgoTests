words= list(input().split())
wordA = list(words[0])
wordB = list(words[1])
wordA.sort()
wordB.sort()

if wordA == wordB:
    print('ANAGRAMS')
else:
    print('NOT ANAGRAMS')

