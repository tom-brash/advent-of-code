import re
from collections import deque, defaultdict

def main():
    print('====Day 8====')
    print('Encountered a patch of tall trees!')
    print('Determining suitability for a treehouse...')
    with open('input', 'r') as open_file:
        input = open_file.read().strip().split('\n')
    trees = {}

    for r, line in enumerate(input):
        row_dict = {}
        for c, char in enumerate(line):
            row_dict[c] = int(char) 
        trees[r] = row_dict

    total = 0
    for r in range(len(input)):
        for c in range(len(input[0])):
            total += check_vis(r, c, trees)

    
    print(f'\n(8-1) Number of trees visible from outside the grid: {total}')

def check_vis(r, c, trees):
    t_height = trees[r][c]
    grid_max_row = len(trees.keys()) - 1
    grid_max_col = len(trees[0].keys()) - 1
    if r == 0 or c == 0 or r == grid_max_row or c == grid_max_col: 
        return 1
    vis = 1
    
    vu = 1
    vd = 1
    vl = 1
    vr = 1
    # check up
    for ro in range(0, r):
        if trees[ro][c] >= t_height:
            vu = 0
    
    for ro in range(r + 1, grid_max_row + 1):
        if trees[ro][c] >= t_height:
            vd = 0

    for co in range(0, c):
        if trees[r][co] >= t_height:
            vl = 0

    for co in range(c + 1, grid_max_col + 1):
        if trees[r][co] >= t_height:
            vr = 0 
    
    if vu + vd + vl + vr >= 1:
        return 1
    else: return 0

        
if __name__ == "__main__":
    main()
