import re
from collections import deque, defaultdict

def main():
    with open('input', 'r') as open_file:
        input = open_file.read()

    print(input)
    grid = {}
    grid_moves = defaultdict(dict)

    for r, row in enumerate(input.split('\n\n')[0].split('\n')):
        for c, ch in enumerate(row):
            if ch in "#.":
                grid[(r, c)] = ch

    instructions = re.findall(r'(?:\d+)|(?:\w)', input.split('\n\n')[1])
    instructions = [int(x) if x not in 'LR' else x for x in instructions ]

    pos = (0, min([p[1] if p[0] == 0 and grid[p] == '.' else 99 for p in grid]), 0)
    
    for x in instructions:
        # print(pos[0], pos[1], pos[2])
        # print(x)
        # print()
        if isinstance(x, str):
            pos = turn(pos, x)
        else:
            pos, grid_movees = move(grid, grid_moves, pos, x)

    print('final_pos')
    print(pos)
    print((pos[0]+1) * 1000 + (pos[1]+1) * 4 + pos[2])

def turn(pos, x):
    row, col, d = pos
    if x == 'R':
        d = (d + 1) % 4
    else:
        d = (d - 1) % 4
    return (row, col, d)

def move(grid, grid_moves, pos, x):
    row, col, d = pos
    for i in range(x):
        n_pos = grid_moves.get((row, col, d), None)
        if n_pos:
            row, col = n_pos 
        else:
            m_dict = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
            t_pos = (row + m_dict[d][0], col + m_dict[d][1])
            if t_pos in grid:
                if grid[t_pos] == "#":
                    grid_moves[(row, col, d)] = (row, col)
                    return (row, col, d), grid_moves
                grid_moves[(row, col, d)] = t_pos
                row, col = t_pos
            else:
                if d == 0:
                    tcol = min([p[1] for p in grid if p[0] == row])
                    trow = row
                elif d == 2:
                    tcol = max([p[1] for p in grid if p[0] == row])
                    trow = row
                elif d == 1:
                    tcol = col
                    trow = min([p[0] for p in grid if p[1] == col])
                elif d == 3:
                    tcol = col
                    trow = max([p[0] for p in grid if p[1] == col])
                if grid[(trow, tcol)] == "#":
                    grid_moves[(row, col, d)] = (row, col)
                    return (row, col, d), grid_moves
                grid_moves[(row, col, d)] = (trow, tcol)
                row, col = trow, tcol
    return (row, col, d), grid_moves


if __name__ == "__main__":
    main()
