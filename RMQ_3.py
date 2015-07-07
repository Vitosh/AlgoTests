import math

def locate_parent(position,levels):
    #Locates a parent of the position, taking into account the levels above.
    for i in range (0 ,levels):
        position = int((position-1)/2)
    return position

def logarithm(n):
    #log base 2 of n is m
    return int(math.log(n,2))

def is_left(number):
    #answers whether the branch is left (true) or right
    if number%2 ==1:
        return True
    else:
        return False

def get_parent_on_levels(node,level):
    #returns the node, on which a parent is located. 
    #or a grandparent, if the level is 2 :)
    while level>0:
        node = int((node-1)/2)
        level-=1
    return node

def set_value(position, number):
    #sets a value in the initial array.
    #then rebuilds part of the tree, to make sure it is still working
    position = starting_position+position
    tree[position] = number

    our_number = number
    our_position = position    
    
    while(True) and our_position != 0:     
        
        if is_left(number):
            compare_with = tree[our_position+1]
        else:
            compare_with = tree[our_position-1]
        
        if number<compare_with:
            our_position = get_parent_on_levels(our_position,1)
            tree[our_position] = our_number
            
        else:
            break      

def create_a_binary_tree(list_first_line):
    #creates a binary tree from the given input
    known_leaves = len(list_first_line)
    total_leaf_size = 2**((len(list_first_line)-1).bit_length())
    
    tree = []
    tree.extend([0]*(total_leaf_size-1))
    tree.extend(list_first_line)
    tree.extend([0]*(total_leaf_size-known_leaves))
    
    start_at = total_leaf_size-2
    
    while start_at>= 0:
        tree[start_at] = min(tree[2*start_at+1], tree[2*start_at+2])
        start_at -= 1
    
    return tree

def parent_in_range(node_parent,a,b,level):
    #checks whether a node is a parent of given 2 other nodes.
    #levels are taken into account as well
    list_children = get_left_and_right_children(node_parent,level)
    if list_children[0]>=a and list_children[1]<=b:
        return True
    return False

def get_left_and_right_children(node, level):
    #gets the child which is in the leftmost position
    #and the child in the rightmost
    #concerning the level
    nodeRightChild = node
    nodeLeftChild = node
    
    while level>0:
        nodeLeftChild = 2*nodeLeftChild + 1
        nodeRightChild  = 2*nodeRightChild +2
        level-=1
    return ([nodeLeftChild, nodeRightChild])

#Input starts here
list_n_and_k = list(input().split())
list_n_and_k = list(map(int, list_n_and_k))

list_first_line = list(input().split())
list_first_line = list(map(int, list_first_line))

total_entries = list_n_and_k[1]
list_orders = []

for i in range (0, total_entries):
    order = []
    order = list(input().split())
    
    if order[0] != "min":
        order[0] = 0
    else:
        order[0] = 1
    
    order[1] = int(order[1])
    order[2] = int(order[2])
    list_orders.append(order)
#Input ends here

tree = create_a_binary_tree(list_first_line)
starting_position = int(len(tree)/2)

def locate_minimal(a, b):
  #locates minimal value within two nodes
    a+= starting_position
    b+= starting_position
    result = []
    
    if a%2 == 0:
        result.append( tree[a])
        a+=1
    if b%2 == 1:
        result.append(tree[b])
        b-=1
    while (a<b):
        level = 1
        while True:
            parent_on_level = get_parent_on_levels(a,level)
            if parent_in_range(parent_on_level,a,b,level):
                level+=1
                last_parent = tree[parent_on_level]
            else:
                break
        level -=1
        
        b_of_small_list = a+(2**(level)-1)
        
        result.append(last_parent)
        a = b_of_small_list+1
        

    return min(result)

for command in list_orders:
    if command[0]:
        list_of_minimals = []
        list_of_minimals = print(locate_minimal(command[1],command[2]))
    else:
        set_value(command[1],command[2])