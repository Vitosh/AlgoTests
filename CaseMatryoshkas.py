n_and_k = list(map(int, list(input().split())))
number_of_chains = n_and_k[1]
number_of_dolls = n_and_k[0]

list_of_chains = []
all_dolls = []

for i in range(0, number_of_chains):
    doll_chain = []
    doll_chain = list(map(int, list(input().split())))
    doll_chain.pop(0)
    doll_chain.sort()
    list_of_chains.append(doll_chain)
    
    all_dolls.extend(doll_chain)

all_dolls.sort()
is_first = True
previous_index_of_doll_chain = -1
result = 0
while number_of_dolls> 0:
    current_doll = all_dolls.pop(0)
    index_of_doll_chain = 0
    
    for doll in list_of_chains:
        if len(doll)==0:
            continue
        
        if doll[0] == current_doll:
            index_of_doll_chain = list_of_chains.index(doll)
            list_of_chains[list_of_chains.index(doll)].pop(0)
            number_of_dolls -= 1
            
            if previous_index_of_doll_chain != index_of_doll_chain:
                result += 2
            
            if is_first:
                result -= 1
                is_first = False
                
            if not len(list_of_chains[list_of_chains.index(doll)])>0:
                result -= 1
               
            previous_index_of_doll_chain = index_of_doll_chain
            break
        
print(result)