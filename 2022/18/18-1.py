import re
from collections import deque, defaultdict

def main():
    with open('input', 'r') as open_file:
        input = open_file.read().strip().split('\n')

    drops = set()
    n_drops = 0

    for x in input:
        nums = tuple([int(a) for a in re.findall(r'\d+', x)])
        drops.add(nums)
        n_drops += 1

    collisions = 0
    for d in drops:
        nb = get_neighbors(d)
        for n in nb:
            if n in drops:
                collisions += 1

    print(f'Surface area: {n_drops * 6 - collisions}')

def get_neighbors(d):
    x, y, z = d
    return ((x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1))

if __name__ == "__main__":
    main()
