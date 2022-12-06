def main():
    with open('day1/1.txt', 'r') as open_file:
        input_data = open_file.read().split(', ')
    
    x = 0
    y = 0
    v = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}
    d = 0

    for i in input_data:
        if i[0] == 'L':
            d = (d - 1) % 4
        else:
            d = (d + 1) % 4
        n = int(i[1:])
        x += v[d][0] * n
        y += v[d][1] * n

    print(abs(x) + abs(y)) 

if __name__ == '__main__':
    main()