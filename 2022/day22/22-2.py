import re
from collections import deque, defaultdict

def main():
    with open('input', 'r') as open_file:
        input = open_file.read()

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

    print(pos)
    print(f'Final answer: {(pos[0]+1) * 1000 + (pos[1]+1) * 4 + pos[2]}')

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
            row, col, d = n_pos 
        else:
            m_dict = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
            t_pos = (row + m_dict[d][0], col + m_dict[d][1])
            if t_pos in grid:
                if grid[t_pos] == "#":
                    grid_moves[(row, col, d)] = (row, col, d)
                    return (row, col, d), grid_moves
                grid_moves[(row, col, d)] = (t_pos[0], t_pos[1], d)
                row, col = t_pos
            else:
                # face "1":
                if row == 0 and col in range(50, 100) and d == 3:
                    n_col = 0
                    face_d = (col - 50)
                    n_row = 150 + face_d
                    n_d = 0
                elif col == 50 and row in range(0, 50) and d == 2:
                    n_col = 0
                    face_d = (49 - row)
                    n_row = 100 + face_d
                    n_d = 0

                # face "2"
                elif col == 50 and row in range(50, 100) and d == 2:
                    n_row = 100
                    face_d = (99 - row)
                    n_col = (49 - face_d)
                    n_d = 1
                
                elif col == 99 and row in range(50, 100) and d == 0:
                    n_row = 49
                    face_d = row - 50
                    n_col = 100 + face_d
                    n_d = 3
                
                # face "3"

                elif col == 99 and row in range(100, 150) and d == 0:
                    n_col = 149
                    face_d = row - 100
                    n_row = 49 - face_d
                    n_d = 2

                elif row == 149 and col in range(50, 100) and d == 1:
                    n_col = 49
                    face_d = 99 - col
                    n_row = 199 - face_d
                    n_d = 2

                # face "4"

                elif col == 49 and row in range(150, 200) and d == 0:
                    n_row = 149
                    face_d = row - 150
                    n_col = 50 + face_d
                    n_d = 3
                
                elif row == 199 and col in range(0, 50) and d == 1:
                    n_row = 0
                    face_d = 49 - col
                    n_col = 149 - face_d
                    n_d = 1

                elif col == 0 and row in range(150, 200) and d == 2:
                    n_row = 0
                    face_d = 199 - row
                    n_col = 99 - face_d
                    n_d = 1

                # face "5"

                elif row == 100 and col in range(0, 50) and d == 3:
                    n_col = 50
                    face_d = col
                    n_row = 50 + face_d
                    n_d = 0
                
                elif col == 0 and row in range(100, 150) and d == 2:
                    n_col = 50
                    face_d = 149 - row
                    n_row = 0 + face_d
                    n_d = 0

                # face "6"

                elif row == 0 and col in range(100, 150) and d == 3:
                    n_row = 199
                    face_d = col - 100
                    n_col = 0 + face_d
                    n_d = 3

                elif col == 149 and row in range(0, 50) and d == 0:
                    n_col = 99
                    face_d = row - 0
                    n_row = 149 - face_d
                    n_d = 2

                elif row == 49 and col in range(100, 150) and d == 1:
                    n_col = 99
                    face_d = 149 - col
                    n_row = 99 - face_d
                    n_d = 2
                
                if grid[(n_row, n_col)] == "#":
                    grid_moves[(row, col, d)] = (row, col, d)
                    return (row, col, d), grid_moves
                grid_moves[(row,col, d)] = (n_row, n_col, n_d)
                row, col, d = n_row, n_col, n_d

    return (row, col, d), grid_moves


if __name__ == "__main__":
    main()
