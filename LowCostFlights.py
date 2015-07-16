list_matrix = []
list_flights = []

int_total_numbers_count = int(input())

for i in range(0, int_total_numbers_count):
    list_matrix.append(list(map(int, input().split())))

fromAirport = 3
toAirport = 2

result_airports = {}
result_airports[fromAirport] = -1 #own airport 

result = []
result = list_matrix[fromAirport]

coming_from_airport = []
airports = []
financial_result = []
while (len(result_airports)<=int_total_numbers_count) and not all(z == 0 for z in result):
    
    minimal_in_array = min(i for i in result if i > 0)
    
    position_of_minimal_in_array = result.index(minimal_in_array)
    
    plane_coming_from_airport =  ((position_of_minimal_in_array+1) // int_total_numbers_count)
    
    print(plane_coming_from_airport)
    
    home_airport = len(result) % position_of_minimal_in_array 
    result[position_of_minimal_in_array] = 0
    keeping_min_position = position_of_minimal_in_array 
    position_of_minimal_in_array = ((position_of_minimal_in_array) % (int_total_numbers_count))
    
    if position_of_minimal_in_array not in result_airports:
        result_airports[position_of_minimal_in_array] = minimal_in_array
        result.extend(list_matrix[position_of_minimal_in_array])
        coming_from_airport.append(plane_coming_from_airport)
        airports.append(position_of_minimal_in_array)
        
        min_range = (result[keeping_min_position]+1)//int_total_numbers_count
        max_range = min_range+int_total_numbers_count
        
        for i in range(min_range, max_range):
            result[i] += minimal_in_array
        
        
        
print('\n',result)
print(result_airports)
print(coming_from_airport)
print(airports)