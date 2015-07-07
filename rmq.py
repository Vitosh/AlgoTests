list_first_line = list(input().split())
list_first_line = list(map(int, list_first_line))
list_first_line.sort()

known_leaves = len(list_first_line)
total_leaf_size = 2**((len(list_first_line)-1).bit_length())

tree = []
tree.extend([0]*(total_leaf_size-1))
tree.extend(list_first_line)
tree.extend([0]*(total_leaf_size-known_leaves))

start_at = total_leaf_size-2

while start_at>= 0:
    tree[start_at] = tree[2*start_at+1] + tree[2*start_at+2]
    start_at -= 1

print(tree)