data = [['a','b'], ['a','c'], ['b','d']]
s = 'c'
for sk in data:
    if sk[1] == s:
        print(sk)
        print(data.index(sk))
        data[data.index(sk)].pop(0)
        print(data)
