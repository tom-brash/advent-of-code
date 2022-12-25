import re
from collections import deque, defaultdict

def main():
    with open('input', 'r') as open_file:
        input = open_file.read().strip().split('\n')
    trees = {}

    for r, line in enumerate(input):
        row_dict = {}
        for c, char in enumerate(line):
            row_dict[c] = int(char) 
        trees[r] = row_dict

    best = 0
    for r in range(len(input)):
        for c in range(len(input[0])):
            vis = check_vis(r, c, trees)
            if vis > best:
                best = vis

    
    print(f'\nIdentifing the best treehouse location...')
    print(f'\n(8-2) Best treehouse has a scenic score of {best}')

def check_vis(r, c, trees):
    t_height = trees[r][c]
    grid_max_row = len(trees.keys()) - 1
    grid_max_column = len(trees[0].keys()) - 1
    
    vu = 0
    vd = 0
    vl = 0
    vr = 0
    # check up
    for ro in range(r - 1, -1, -1):
        if trees[ro][c] < t_height:
            vu += 1
        else:
            vu += 1
            break
    
    for ro in range(r + 1, grid_max_row + 1):
        if trees[ro][c] < t_height:
            vd += 1
        else:
            vd += 1
            break

    for co in range(c - 1, -1, -1):
        if trees[r][co] < t_height:
            vl += 1
        else:
            vl += 1
            break

    for co in range(c + 1, grid_max_column + 1):
        if trees[r][co] < t_height:
            vr += 1 
        else:
            vr += 1
            break
    
    return vu * vd * vl * vr
        
if __name__ == "__main__":
    main()
