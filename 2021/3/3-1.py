def main():

    with open('3/3.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')
    
    x = 0
    for i in range(len(input_data)):
        pass
    
    gamma = '0b'
    epsilon = '0b'
    for x in range(len(input_data[0])):        
        z = 0
        o = 0
        for i in input_data:
            if i[x] == '0':
                z += 1
            else:
                o += 1
        if o > z:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'

    print(int(gamma, 2) * int(epsilon, 2))


if __name__ == '__main__':
    main()