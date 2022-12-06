'''
Day 20-1: Checking a map for all nearby rooms

Here I looked at a couple of tips to try and learn new skills - building this as a network graph
was a great option that alleviated most of the complexity. Keeping track of grups and 'ends' is
done using sets, but the interesting thing here is using imaginary numbers as the x plane, which
makes it even more efficient
'''

import networkx

def main():
    with open('day20/20-1-input.txt', 'r') as open_file:
        directions = open_file.read()[1:-1]
    
    maze = networkx.Graph()

    positions = {0}
    group_memory = []
    starts = {0}
    ends = set()
    v_map = {'N': -1, 'S': 1, 'W': -1j, 'E': 1j}

    for c in directions:
        if c == '|':
            ends.update(positions)
            positions = starts            
        elif c in 'NSEW':
            v = v_map[c]
            maze.add_edges_from((p, p + v) for p in positions)
            positions = {p + v for p in positions}
        elif c == '(':
            group_memory.append((starts, ends))
            starts = positions
            ends = set()
        elif c == ')':
            positions.update(ends)
            starts, ends = group_memory.pop()
    
    lengths = networkx.algorithms.shortest_path_length(maze, 0)

    print(max(lengths.values()))


if __name__ == '__main__':
    main()

