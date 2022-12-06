'''
DAY 3-2: Check for hitting trees on different vectors

We can reuse the logic from 3-1. However, we move the bulk of the code to 
a function that takes a vector input, to allow us to check each of the input vectors
and keep track of how many trees are hit.
'''

def main():

    with open('day3/3-1-input.txt', 'r') as input_data_file:
        input_data = input_data_file.read()

    rows = input_data.split('\n')
    rows.remove('')

    total_cols = len(rows[0])
    cols = []
    for i in range(total_cols):
        col = ''
        for row in rows:
            col = col + row[i]
        cols.append(col)

    slopes = [(1,1), (3, 1), (5, 1), (7, 1), (1, 2)]
    tree_mult = 1
    
    for slope in slopes:
        tree_mult *= check_trees(slope[0], slope[1], cols, total_cols, len(rows))
    
    print(tree_mult)

def check_trees(h, v, cols, total_cols, num_rows):
    
    pos = [0, 0]

    trees = 0
    while pos[0] < num_rows:
        c = pos[1] % total_cols
        r = pos[0]
        if cols[c][r] == '#':
            trees += 1
        pos[0] = pos[0] + v
        pos[1] = pos[1] + h

    return(trees)    



if __name__ == '__main__':
    main()   