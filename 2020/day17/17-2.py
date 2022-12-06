'''
DAY 17-2: Conway's 4D game of life

This is just a 4 dimensional extension of the first problem (3 dimensions). 

The way that 17-1 is drawn up, the 4D extension is straightforward. Each function
is just adapted to work in an extra dimension (w, x, y, z). We need to loop over
each of the cells in the four dimensions and check the 80 neighbors of each cell, 
but the logic is consistent with 17-1
'''

import numpy as np

def main():
    with open('day17/17-1-input.txt', 'r') as input_data_file:
        input_data = input_data_file.read()

    input_rows = input_data.split('\n')
    input_rows = [convert_input(x) for x in input_rows]

    conway_matrix = np.array([[input_rows]])  # reading in the input as a [1, 1, x, y] input
    
    for i in range(6):
        print('Running round ' + str(i + 1) + '...')
        conway_matrix = extend_matrix(conway_matrix)
        conway_matrix = run_conway_cycle(conway_matrix)
        conway_matrix = consolidate_matrix(conway_matrix)
    
    print(np.sum(conway_matrix))
    

def convert_input(line):
    return_line = []
    for char in line:
        if char == '#':
            return_line.append(1)
        else:
            return_line.append(0)
    return return_line

def extend_matrix(mat):
    dimensions = 4
    for i in range(dimensions):
        add_stack_shape = list(mat.shape)
        add_stack_shape[i] = 1
        add_stack = np.zeros(tuple(add_stack_shape))
        mat = np.concatenate((mat, add_stack), axis=i)
        mat = np.concatenate((add_stack, mat), axis=i)
    
    return mat


def consolidate_matrix(mat):
    stable = False
    while stable == False:
        starting_matrix = np.copy(mat)
        if np.count_nonzero(mat[0, :, :, :]) == 0:
            mat = mat[1:, :, :, :]
        if np.count_nonzero(mat[-1, :, :]) == 0:
            mat = mat[:-1, :, :, :]

        if np.count_nonzero(mat[:, 0, :, :]) == 0:
            mat = mat[:, 1:, :]
        if np.count_nonzero(mat[:, -1, :, :]) == 0:
            mat = mat[:, :-1, :, :]

        if np.count_nonzero(mat[:, :, 0, :]) == 0:
            mat = mat[:, :, 1:, :]
        if np.count_nonzero(mat[:, :, -1, :]) == 0:
            mat = mat[:, :, :-1, :]

        if np.count_nonzero(mat[:, :, :, 0]) == 0:
            mat = mat[:, :, :, 1:]
        if np.count_nonzero(mat[:, :, :, -1]) == 0:
            mat = mat[:, :, :, :-1]

        if np.array_equal(starting_matrix, mat) == True:
            stable = True

    return(mat)


def run_conway_cycle(mat):
    updated_matrix = np.copy(mat)
    for w in range(mat.shape[0]):
        for x in range(mat.shape[1]):
            for y in range(mat.shape[2]):
                for z in range(mat.shape[3]):
                    nearby_on = sum_neighbors(mat, w, x, y, z)
                    if mat[w][x][y][z] == 1:
                        if not (nearby_on == 2 or nearby_on == 3):
                            updated_matrix[w][x][y][z] = 0
                    else:
                        if nearby_on == 3:
                            updated_matrix[w][x][y][z] = 1
    return updated_matrix


def sum_neighbors(mat, w, x, y, z):
    total = 0 - mat[w][x][y][z]
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            for k in [-1, 0, 1]:
                for l in [-1, 0, 1]:
                    if (w + i) >= 0 and (w + i) < mat.shape[0]:
                        if (x + j) >= 0 and (x + j) < mat.shape[1]:
                            if (y + k) >=0 and (y + k) < mat.shape[2]:
                                if (z + l) >=0 and (z + l) < mat.shape[3]:
                                    total += mat[w + i][x + j][y + k][z + l]
    return total 


if __name__ == "__main__":
    main()     

