def main():

    with open('2/2.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')
    
    h = 0
    de = 0
    aim = 0

    for i in input_data:
        
        d, x = i.split()
        x = int(x)
        if d == 'forward':
            h += x
            de += aim * x
        if d == 'down':
            aim += x
        if d == 'up':
            aim -= x

    print(h * de)


if __name__ == '__main__':
    main()