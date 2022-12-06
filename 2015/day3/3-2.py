def main():
    with open('day3/3.txt', 'r') as open_file:
        input_data = open_file.read()


    x = y = r_x = r_y =0
    visited = set()
    visited.add((x, y))
    vecs = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}
    
    for i, c in enumerate(input_data):
        if i % 2 == 0:
            x += vecs[c][0]
            y += vecs[c][1]
            visited.add((x, y))
        else:
            r_x += vecs[c][0]
            r_y += vecs[c][1]
            visited.add((r_x, r_y))
        
    
    print(len(visited))

if __name__ == '__main__':
    main()