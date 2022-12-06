def main():

    with open('2/2.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')
    
    h = 0
    de = 0
    print(input_data)

    for i in input_data:
        d = i.split()[0]
        x = i.split()[1]
        if d == 'forward':
            h += int(x)
        if d == 'down':
            de += int(x)
        if d == 'up':
            de -= int(x)

    print(h * de)


if __name__ == '__main__':
    main()