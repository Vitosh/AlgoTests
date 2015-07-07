import math

def locate_parent(position,levels):
    
    for i in range (0 ,levels):
        position = int((position-1)/2)
    return position

def logarithm(n):
    #log base 2 of n is m
    return int(math.log(n,2))

def get_left_and_right_children(node, level):
    nodeRightChild = node
    nodeLeftChild = node
    
    while level>0:
        nodeLeftChild = 2*nodeLeftChild + 1
        nodeRightChild  = 2*nodeRightChild +2
        level-=1
    return ([nodeLeftChild, nodeRightChild])

tree = [2, 2, 3, 4, 2, 3, 4, 11, 4, 7, 2, 3, 7, 17, 4, 19, 11, 15, 4, 7, 13, 11, 2, 3, 5, 12, 7, 23, 17, 4, 6]
starting_position = int(len(tree)/2)

def get_parent_on_levels(node,level):
    while level>0:
        node = int((node-1)/2)
        level-=1
    return node

def parent_in_range(node_parent,a,b,level):
    list_children = get_left_and_right_children(node_parent,level)
    if list_children[0]>=a and list_children[1]<=b:
        return True
    return False

def locate_minimal(a, b):
    a+= starting_position
    b+= starting_position
    result = []

    if a%2 == 0:
        small_list_1 = [a]
        result.append(small_list_1)
        a+=1
    if b%2 == 1:
        small_list_2 = [b]
        result.append(small_list_2)
        b-=1
    
    while (a<b):
        level = 1
        while parent_in_range(get_parent_on_levels(a,level),a,b,level):
            level+=1
        
        small_list = []
        b_of_small_list = a+(2**(level-1)-1)
        small_list.append(a)
        small_list.append(b_of_small_list)
        result.append(small_list)
        a = b_of_small_list+1    
    
    return result
    
minimals = locate_minimal(5,10)
values_to_compare = []
for list in minimals:
    if len(list) == 1:
        values_to_compare.append(tree[list[0]])
    else:
        length_of_result = (list[1]-list[0])+1
        levels = logarithm(length_of_result)
        result = locate_parent(list[0],levels)
        values_to_compare.append(tree[result])

print(min(values_to_compare))
