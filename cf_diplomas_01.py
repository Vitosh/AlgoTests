int_total_diplomas = int(input())

degree_1 = list(map(int, list(input().split())))
degree_2 = list(map(int, list(input().split())))
degree_3 = list(map(int, list(input().split())))

min_degree_1 = degree_1[0]
max_degree_1 = degree_1[1]
min_degree_2 = degree_2[0]
max_degree_2 = degree_2[1]
min_degree_3 = degree_3[0]
max_degree_3 = degree_3[1]

degree_1_total = min_degree_1
degree_2_total = min_degree_2
degree_3_total = min_degree_3

def calculate_diplomas(int_total_diplomas,degree_1_total,degree_2_total, degree_3_total,max_degree_1,max_degree_2):

    if int_total_diplomas <= degree_2_total + degree_3_total + max_degree_1:
        degree_1_total = int_total_diplomas - degree_2_total - degree_3_total
        print(degree_1_total,degree_2_total,degree_3_total)
        return
    
    else :
        degree_1_total = max_degree_1
        
    if int_total_diplomas <= degree_1_total + degree_3_total + max_degree_2:
        degree_2_total = int_total_diplomas - degree_1_total - degree_3_total
        print(degree_1_total,degree_2_total,degree_3_total)
        return        
    else:
        degree_2_total = max_degree_2
        
    degree_3_total = int_total_diplomas - degree_2_total - degree_1_total
    print(degree_1_total,degree_2_total,degree_3_total)
    return




calculate_diplomas(int_total_diplomas,degree_1_total,degree_2_total, degree_3_total,max_degree_1,max_degree_2)