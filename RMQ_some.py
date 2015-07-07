import math

def logarithm(n):
    #log base 2 of n is m
    return math.log(n,2)

def locate_parent(position,levels):
    
    for i in range (0 ,levels):
        position = int((position-1)/2)
    return position
       
list_first_line = list(input().split())
list_first_line = list(map(int, list_first_line))




known_leaves = len(list_first_line)
total_leaf_size = 2**((len(list_first_line)-1).bit_length())

tree = []
tree.extend([0]*(total_leaf_size-1))
tree.extend(list_first_line)
tree.extend([0]*(total_leaf_size-known_leaves))

start_at = total_leaf_size-2
starting_position = start_at

while start_at>= 0:
    tree[start_at] = min(tree[2*start_at+1], tree[2*start_at+2])
    start_at -= 1

#print(tree)
