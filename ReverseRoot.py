import sys, re
from math import sqrt as sq

def find_numbers(f):
    for line in f:
        for word in line.split():
            if word.isdigit():
                yield float(word)

lst = list(find_numbers(sys.stdin))
lst.reverse()
for x in lst:
    print('%.4f' % sq(x))