import copy

def main():

    with open('3/3.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')
    
    x = 0
    for i in range(len(input_data)):
        pass
    
    b = '0b'
    c = '0b'

    oxygen = '0b'
    co2 = '0b'
    
    # GET OXYGEN VALUE
    search_data = copy.deepcopy(input_data)
    for x in range(len(input_data[0])):        
        if len(search_data) == 1:
            oxygen += search_data[0]
        target = 'a'
        z = 0
        o = 0
        for i in search_data:
            if i[x] == '0':
                z += 1
            else:
                o += 1
        if z > o:
            target = '0'
        else:
            target = '1'
        search_data = [v for v in search_data if v[x] == target]

    if oxygen == '0b':
        oxygen += search_data[0]

    # GET CO2 VALUE
    search_data = copy.deepcopy(input_data)
    for x in range(len(input_data[0])):                
        if len(search_data) == 1:
            co2 += search_data[0]
        target = 'a'
        z = 0
        o = 0
        for i in search_data:
            if i[x] == '0':
                z += 1
            else:
                o += 1
        if o < z:
            target = '1'
        else:
            target = '0'
        search_data = [v for v in search_data if v[x] == target]
    
    if co2 == '0b':
        co2 += search_data[0]

    print(int(oxygen, 2) * int(co2, 2))


if __name__ == '__main__':
    main()