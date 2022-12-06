with open('day6/6-1-input.txt', 'r') as input_file:
    input_data = input_file.read()

raw_orbits = input_data.split('\n')
raw_orbits.remove('')

orbits = [i.split(')') for i in raw_orbits]


distance_from_com = {'COM':0}
for orbit in orbits:
    distance_from_com[orbit[1]] = 0

while True:
    total_orbits = sum(distance_from_com.values())
    for orbit in orbits:
        distance_from_com[orbit[1]] = distance_from_com[orbit[0]] + 1

    if sum(distance_from_com.values()) - total_orbits == 0:
        break

#print(distance_from_com)
print('Total orbits:', sum(distance_from_com.values()))
