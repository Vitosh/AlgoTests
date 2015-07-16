n_and_k = list(map(int, list(input().split())))
number_of_chains = n_and_k[1]
number_of_dolls = n_and_k[0]

list_of_chains = []
all_dolls = []
result = 0
previous_index_of_doll_chain = -1

for i in range(0, number_of_chains):
    doll_chain = []
    doll_chain = list(map(int, list(input().split())))
    doll_chain.pop(0)
    doll_chain.sort()
    list_of_chains.append(doll_chain)
    all_dolls.extend(doll_chain)

all_dolls.sort()

while number_of_dolls> 0:
    current_doll = all_dolls.pop(0)
    index_of_doll_chain = 0
    
    for doll in list_of_chains:
        if len(doll)==0:
            continue

        if doll[0] == current_doll:
            current_index_of_doll_chain = list_of_chains.index(doll)
            
            list_of_chains[list_of_chains.index(doll)].pop(0)
            number_of_dolls -= 1
        if previous_index_of_doll_chain != current_index_of_doll_chain:
            result += 1
        
        previous_index_of_doll_chain = current_index_of_doll_chain
    print(list_of_chains)
        
#print(result)
