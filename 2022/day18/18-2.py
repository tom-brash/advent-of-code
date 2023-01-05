import re
from collections import deque, defaultdict

def main():
    with open('input', 'r') as open_file:
        input = open_file.read().strip().split('\n')

    drops = set()
    max_size = 0

    for x in input:
        nums = tuple([int(a) for a in re.findall(r'\d+', x)])
        if max(nums) > max_size:
            max_size = max(nums)
        drops.add(nums)

    external = set()
    internal = set()

    surface_area = 0
    for d in drops:
        nb = get_neighbors(d)
        for n in nb:
            if n in drops or n in internal:
                continue
            if n in external:
                surface_area += 1
                continue
            is_external, visited = bfs(n, max_size, drops, external, internal)
            if is_external:
                external = external.union(visited)
                surface_area += 1
            else:
                internal = internal.union(visited)

    print(f"\n(18-2) External surface area of droplet: {surface_area}")

def get_neighbors(d):
    x, y, z = d
    return ((x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1))

def bfs(start, max_size, grid, external, internal):
    sq = deque([(start, 0)])
    best_states = {}
    visited = set()
    while sq:
        loc, d = sq.popleft()
        x, y, z = loc
        visited.add((x, y, z))
        if min(x,y,z) <= 0 or max(x,y,z) >= max_size:
            return True, visited
        if (x, y, z) in external:
            return True, visited
        if (x, y, z) in internal:
            return False, visited
        best_previous = best_states.get((x, y, z), 1000)
        if d >= best_previous:
            continue
        best_states[(x, y, z)] = d
        sq.extend(get_valid_moves(x, y, z, d, grid))
    return False, visited

def get_valid_moves(x, y, z, d, grid):
    options = []
    for n in get_neighbors((x, y, z)):
        if n not in grid:
            options.append((n, d + 1))
    return options

if __name__ == "__main__":
    main()
