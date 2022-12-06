def main():
    with open('day2/2.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')
    
    numpad, width = construct_numpad(9)
    x = 1
    y = 1
    v = {'U': (0, -1), 'R': (1, 0), 'D': (0, 1), 'L': (-1, 0)}
    code = ''

    for i in input_data:
        for c in i:
            x += v[c][0]
            y += v[c][1]
            if x < 0:
                x = 0
            if x > width:
                x = width
            if y < 0:
                y = 0
            if y > width:
                y = width
        code += str(numpad[(x,y)])
    
    print(code)
        



def construct_numpad(n):
    x = y = 0
    l = n ** 0.5
    d = {}
    for i in range(n):
        d[(x, y)] = i + 1
        x = x + 1
        if x == l:
            x = 0
            y = y + 1
    return d, l - 1


if __name__ == '__main__':
    main()