'''
Day 20-2: Checking a map for all nearby rooms

The networkx construction from part A makes this trivial
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

    print(len([l for l in lengths.values() if l >= 1000]))


if __name__ == '__main__':
    main()

