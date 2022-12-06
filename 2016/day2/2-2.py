def main():
    with open('day2/2.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')
    
    numpad = {(2, 0): '1', 
        (1, 1): '2', (2, 1): '3', (3, 1): '4',
        (0, 2): '5', (1, 2): '6', (2, 2): '7', (3, 2): '8', (4, 2): '9',
        (1, 3): 'A', (2, 3): 'B', (3, 3): 'C',
        (2, 4): 'D'}
    
    x = 0
    y = 2
    v = {'U': (0, -1), 'R': (1, 0), 'D': (0, 1), 'L': (-1, 0)}
    code = ''

    for i in input_data:
        for c in i:
            x_p = x + v[c][0]
            y_p = y + v[c][1]
            if (x_p, y_p) in numpad:
                x = x_p
                y = y_p
        code += str(numpad[(x,y)])
    
    print(code)
        

if __name__ == '__main__':
    main()