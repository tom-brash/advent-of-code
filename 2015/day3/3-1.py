def main():
    with open('day3/3.txt', 'r') as open_file:
        input_data = open_file.read()

    x = 0
    y = 0
    visited = set()
    visited.add((x, y))
    vecs = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}
    
    for c in input_data:
        x += vecs[c][0]
        y += vecs[c][1]
        visited.add((x, y))
    
    print(len(visited))

if __name__ == '__main__':
    main()