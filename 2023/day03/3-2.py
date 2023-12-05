import re
from collections import defaultdict
from pprint import pprint

def is_real_number(grid, i, j, l):
    for y in [-1, 1]:
        for x in range(j-1, j+l+1):
            if grid[(i+y,x)] == '@':
                return (i+y, x)
    if grid[(i, j-1)] == '@':
        return (i, j-1)
    if grid[(i, j+l)] == '@':
        return (i, j+l)

    return False

def main():
    print('==== Day 3 ====')
    with open('input', 'r') as open_file:
	    lines = open_file.read().strip().split('\n')

    width = len(lines[0])
    height = len(lines)
    grid = defaultdict(lambda: '.')

    gears = defaultdict(list)

    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == '*':
                c = '@'
            else: c = '.'
            grid[(i,j)] = c

    total = 0

    for i, line in enumerate(lines):
        nums = re.finditer(r'\d+', line)
        for n in nums:
            x = is_real_number(grid, i, n.start(), n.end() - n.start())
            if x:
                gears[x].append(n.group(0))

    for l in gears.values():
        if len(l) == 2:
            total += int(l[0]) * int(l[1])
    print(total)


if __name__ == "__main__":
	main()
