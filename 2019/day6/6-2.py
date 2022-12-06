def main():

    with open('day6/6-1-input.txt', 'r') as input_file:
        input_data = input_file.read()

    raw_orbits = input_data.split('\n')
    raw_orbits.remove('')

    orbits = [i.split(')') for i in raw_orbits]

    santa_path = find_path('SAN', orbits)
    you_path = find_path('YOU', orbits)

    for i in range(max(len(santa_path), len(you_path))):
        if santa_path[-(i+1)] == you_path[-(i+1)]:
            continue
        else:
            duplicate_path_distance = i
            break

    min_distance = len(you_path) - (duplicate_path_distance)+ len(santa_path) - (duplicate_path_distance) - 2
    print(min_distance)


def find_path(object, orbits):
    return_path = [object]

    while 'COM' not in return_path:
        for orbit in orbits:
            if orbit[1] == return_path[-1]:
                return_path.append(orbit[0])
                break

    return return_path


if __name__ == '__main__':
    main()

