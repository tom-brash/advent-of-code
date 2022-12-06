def main():
    with open('day1/1.txt', 'r') as open_file:
        input_data = open_file.read().split(', ')
    
    x = 0
    y = 0
    v = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}
    d = 0
    
    visited_locs = set((0, 0))
    found = False

    for i in input_data:
        if found:
            break
        if i[0] == 'L':
            d = (d - 1) % 4
        else:
            d = (d + 1) % 4
        n = int(i[1:])
        for j in range(n):
            x += v[d][0]
            y += v[d][1]
            if (x, y) in visited_locs:
                print('Visited location at', x, y)
                print(abs(x) + abs(y))
                found = True
                break
            visited_locs.add((x, y))
        

if __name__ == '__main__':
    main()