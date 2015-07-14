list_matrix = []
list_flights = []

int_total_numbers_count = int(input())

for i in range(0, int_total_numbers_count):
    list_matrix.append(list(map(int, input().split())))

fromAirport = 3
toAirport = 2
#example 4

#int_total_queries = int(input())


#for i in range(0, int_total_queries):
    #list_flights.append(list(map(int, input().split())))

result = []
result = list_matrix[3]
print(result)