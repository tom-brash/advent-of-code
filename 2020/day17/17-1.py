'''
DAY 17-1: Conway's 3D game of life

This problem is essentially a 3-D version of Conway's game of life played out on
an infinite grid. We use numpy arrays to create n-dimensional arrays

Before coding the actual behavior of the cubes, we first consider how much the 'active' 
grid size could possible change. At maximum, it could extend 1 cube in each direction. It could,
however, shrink by an unliimited amount (to a single point) - there's nothing preventing a 
Conway grid that annihilates itself.

We create two helper functions. One extends the grid in all directions with inactive cells, as
these are the cells that need to be checked. The second condenses the grid if a slice at the end
of the grid (in any of the dimensions) is filled with inactive cells. This second function will repeat
until we are down to only the 'active' area of the infinite grid.

With these helper functions, we can easily simulate a cylce of the game of life as:
 - extend grid in every dimension
 - create a copy of the grid
 - check the number of active neighbors and update in the copy accordingly
 - return the copy and condense it to the active area

We can then just sum the grid after six cycles
'''

import numpy as np

def main():
    with open('day17/17-1-input.txt', 'r') as input_data_file:
        input_data = input_data_file.read()

    input_rows = input_data.split('\n')
    input_rows = [convert_input(x) for x in input_rows]

    conway_matrix = np.array([input_rows]) 
    
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
    for i in range(3):
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
        if np.count_nonzero(mat[0, :, :]) == 0:
            mat = mat[1:, :, :]
        if np.count_nonzero(mat[-1, :, :]) == 0:
            mat = mat[:-1, :, :]

        if np.count_nonzero(mat[:, 0, :]) == 0:
            mat = mat[:, 1:, :]
        if np.count_nonzero(mat[:, -1, :]) == 0:
            mat = mat[:, :-1, :]

        if np.count_nonzero(mat[:, :, 0]) == 0:
            mat = mat[:, :, 1:]
        if np.count_nonzero(mat[:, :, -1]) == 0:
            mat = mat[:, :, :-1]

        if np.array_equal(starting_matrix, mat) == True:
            stable = True

    return(mat)


def run_conway_cycle(mat):
    updated_matrix = np.copy(mat)
    for x in range(mat.shape[0]):
        for y in range(mat.shape[1]):
            for z in range(mat.shape[2]):
                nearby_on = sum_neighbors(mat, x, y, z)
                if mat[x][y][z] == 1:
                    if not (nearby_on == 2 or nearby_on == 3):
                        updated_matrix[x][y][z] = 0
                else:
                    if nearby_on == 3:
                        updated_matrix[x][y][z] = 1
    return updated_matrix

def sum_neighbors(mat, x, y, z):
    total = 0 - mat[x][y][z]
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            for k in [-1, 0, 1]:
                if (x + i) >= 0 and (x + i) < mat.shape[0]:
                    if (y + j) >= 0 and (y + j) < mat.shape[1]:
                        if (z + k) >=0 and (z + k) < mat.shape[2]:
                            total += mat[x + i][y + j][z + k]
    return total 


if __name__ == "__main__":
    main()     

