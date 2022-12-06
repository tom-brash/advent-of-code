from collections import defaultdict

def main():
    with open('day11/11.txt', 'r') as open_file:
        instructions = open_file.read().split(',')
    
    x = 0
    y = 0
    
    vecs = {'n': (0, -2), 'ne': (1, -1), 'se': (1, 1), 's': (0, 2), 'sw': (-1, 1), 'nw': (-1, -1)}

    origin = (0, 0)
    
    for i in instructions:
        v = vecs[i]
        x += v[0]
        y += v[1]
    
    terminal = (x, y)

    print(hex_distance(origin, terminal))
        

def hex_distance(origin, terminal):
    dx = abs(origin[0] - terminal[0])
    dy = abs(origin[1] - terminal[1])
    return dx + max(0, (dy-dx) / 2)

        

if __name__ == '__main__':
    main()