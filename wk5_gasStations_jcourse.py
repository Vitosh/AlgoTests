trip_distance = int(input())
tank_size = int(input())
gas_stations_count = int(input())

stations_initial = []

for i in range(0, gas_stations_count):
    stations_initial.append(int(input()))

stations_initial.append(trip_distance)
petrol_currently = tank_size

result = []
distances = []
distances.append(stations_initial[0])

for i in range(1, len(stations_initial)):
    distances.append(stations_initial[i]-stations_initial[i-1])

for i in range(0, len(distances)):
    if petrol_currently < distances[i]:
        #refilling the petrol
        petrol_currently = tank_size
        result.append(stations_initial[i-1])
    petrol_currently -= distances[i]
for i in range(0,len(result)):
    print(result[i])