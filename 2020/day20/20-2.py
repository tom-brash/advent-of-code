'''
DAY 20-2: Solving a jigsaw and hunting for sea monsters

The second part involves the entire grid, and so involves actually solving the jigsaw
puzzle. This is non-trivial, but given that each piece only has a single possible match
in each direction, much of the complexity involves just getting the orientation (and flips)
correct for each piece.

This version works by locking in a first corner in the top left (0, 0) of the grid, and
building out from there - finding the most recently appended side and finding the matching
tile to include.

Once the grid is completed, the 'borders' of each tile are removed to make a smaller grid.
The actual searching for sea monsters is trivial - the pattern is hard coded into the 
function and each cell is tested to see if it is the start of the pattern.

The logic of the code is relatively sound, but clumsy in implementation of helper functions.
Note that several things in the underlying structure have been changed from 20-1 (e.g. only
four sides are stored, not their reverses)
''' 

import re
import pprint
import copy

def main():
    with open('day20/20-1-input.txt', 'r') as input_file:
        input_data = input_file.read()
    
    # read in data and transform into dictionary
    tile_data = input_data.split('\n\n')
    tile_dict = tiles_to_dict(tile_data)

    # find the matches and the corners
    tile_dict = find_matches(tile_dict)
    corners = []
    for tile in tile_dict:
        check = len(tile_dict[tile]['matches'])
        if check == 2:
            corners.append(tile)

    # pull the grid together as a single grid
    jigsaw = assemble_grid(tile_dict, corners)
    
    # remove the borders of the jigsaw
    jigsaw_columns_removed = []
    for i in range(len(jigsaw)):
        new_line = []
        for j in range(len(jigsaw[0])):
            if not (j % 10 == 0 or j % 10 == 9):
                new_line.append(jigsaw[i][j])
        jigsaw_columns_removed.append(new_line)
    
    jigsaw_final = []
    for i in range(len(jigsaw)):
        if not (i % 10 == 0 or i % 10 == 9):
            jigsaw_final.append(jigsaw_columns_removed[i])

    # hunt for sea monsters
    # each orientation is checked: only one should contain sea monsters
    max_sm = 0
    for _ in range(4):
        jigsaw_final = rot90(jigsaw_final)
        num_monsters = find_sea_monsters(jigsaw_final)
        if num_monsters > max_sm:
            max_sm = num_monsters

    jigsaw_final = flip(jigsaw_final)
    for _ in range(4):
        jigsaw_final = rot90(jigsaw_final)
        num_monsters = find_sea_monsters(jigsaw_final)
        if num_monsters > max_sm:
            max_sm = num_monsters

    # print results
    total_hash = 0
    for row in jigsaw_final:
        total_hash += row.count('#')
    print('total hash: ', str(total_hash))
    print('total sea monsters: ', str(max_sm))
    choppy_water = total_hash - max_sm * 15
    print('choppy water: ', str(choppy_water))


# search a finished grid (without borders) for sea monsters
def find_sea_monsters(jigsaw):
    jigsaw_copy = copy.deepcopy(jigsaw)
    # hard code the sea monster pattern
    sea_monster = [[1, 0, '_'], [2, 1, '\\'], [2, 4, '/'], [1, 5,'_'], [1, 6, '_'], [2, 7,'\\'], [2, 10,'/'], [1, 11, '_'], [1, 12, '_'], [2,13, '\\'], [2, 16, '/'], [1, 17, '/'], [1, 18, '0'], [1, 19, '>'], [0, 18, '_']] 
    monster_length = 19
    monster_height = 2          
    found_monsters = 0
    for row in range(len(jigsaw)):
        for col in range(len(jigsaw)):
            if row + monster_height < len(jigsaw) and col + monster_length < len(jigsaw):
                found_monster = True
                for loc in sea_monster:
                    if jigsaw[row + loc[0]][col + loc[1]] != '#':
                        found_monster = False
                if found_monster == True:
                    found_monsters += 1
                    for loc in sea_monster:
                        jigsaw_copy[row + loc[0]][col + loc[1]] = loc[2]  # visualize the monsters
    
    # print out the grid to see the monsters
    for i in range(len(jigsaw_copy)):
        jigsaw_copy[i] = ['~' if x == '#' else x for x in jigsaw_copy[i]]
        jigsaw_copy[i] = [' ' if x == '.' else x for x in jigsaw_copy[i]]
    
    
    if found_monsters > 0:
        for row in jigsaw_copy:
            print(''.join(row))
    return found_monsters

# transform input to dictionary
def tiles_to_dict(tile_data):
    tile_dictionary = {}
    for tile in tile_data:
        tile_num = re.search(r'([0-9]+)\:', tile).group(1)
        side_0 = tile.split('\n')[1]
        side_1 = get_side(tile, 'right')
        side_2 = tile.split('\n')[-1]
        side_3 = get_side(tile, 'left')
        orientation = ''
        sides = [side_0, side_1, side_2, side_3]
        details = [[char for char in x] for x in tile.split('\n')[1:]]
        tile_dictionary[tile_num] = {'sides': sides, 'orientation':orientation, 'details':details}
    return tile_dictionary
        

# find matches for sides
def find_matches(tile_dict):
    for key in tile_dict.keys():
        possible_matches = []
        key_sides = tile_dict[key]['sides']
        for j, k_side in enumerate(key_sides):
            for key_s in tile_dict.keys():
                if key != key_s:
                    for i, side in enumerate(tile_dict[key_s]['sides']):                        
                        if k_side == side:  
                                possible_matches.append([key_s, j, i])
                        if k_side == side[::-1]:
                                possible_matches.append([key_s, j, i])
        tile_dict[key]['matches'] = possible_matches
    return tile_dict


# helper function to get left or right sides of tile
def get_side(tile, orientation):
    if orientation == 'left':
        i = 0
    else:
        i = -1
    side = ''
    for j in tile.split('\n')[1:]:
        side += j[i]
    return side


# primary function to assemble the jigsaw grid
def assemble_grid(tile_dict, corners):
    # create blank grid
    tile_len = len(tile_dict[list(tile_dict.keys())[0]]['details'])
    tile_no = int(len(tile_dict) ** 0.5)
    full_grid_row = ['*'] * tile_len * tile_no
    full_grid = []
    for _ in range(tile_no * tile_len):
        full_grid.append(copy.deepcopy(full_grid_row))

    # place the first corner piece
    first_piece = corners[0]
    req_orientation = orient_first_corner(tile_dict[first_piece]['matches'])    
    oriented_tile = orient(tile_dict[first_piece]['details'], req_orientation)
    
    for y in range(tile_len):
        for x in range(tile_len):
            full_grid[y][x] = oriented_tile[y][x]

    # set up list to keep track of which tiles have been placed
    placed_tiles = [first_piece]
    
    # place all remaining tiles
    for i in range(tile_no):
        if i != 0:
            # start the row by placing the leftmost cell attached to the one above it
            last_row_up = ''.join(full_grid[i * tile_len - 1][:tile_len])
            for tile in tile_dict:
                if tile not in placed_tiles:
                    for s, side in enumerate(tile_dict[tile]['sides']):
                        if side == last_row_up:
                            oriented_tile = orient_up(tile_dict[tile]['details'], s)
                            placed_tiles.append(tile)
                        if side[::-1] == last_row_up:
                            oriented_tile = orient_up(tile_dict[tile]['details'], s, reverse=True)
                            placed_tiles.append(tile)
                            
            for y in range(tile_len):
                for x in range(tile_len):
                    full_grid[y + i * tile_len][x] = oriented_tile[y][x]

        # place the remainder of the row
        for j in range(tile_no - 1):
            last_col = ''
            for end in range(tile_len):
                last_col += full_grid[i * tile_len + end][j * tile_len + tile_len - 1]
            
            for tile in tile_dict:
                if tile not in placed_tiles:
                    for s, side in enumerate(tile_dict[tile]['sides']):
                        if side == last_col:
                            oriented_tile = orient_left(tile_dict[tile]['details'], s)
                            placed_tiles.append(tile)
                        if side[::-1] == last_col:
                            oriented_tile = orient_left(tile_dict[tile]['details'], s, reverse=True)
                            placed_tiles.append(tile)  
            for y in range(tile_len):
                for x in range(tile_len):
                    full_grid[y + i * tile_len][x + (j + 1) * tile_len] = oriented_tile[y][x]  
    
    return full_grid


# get the first corner facing the right direction
# note that this uses an otherwise obselete 'orient' function which was previously being used elsewhere
# this could be simplified dramatically in a rewrite, but it already exists
def orient_first_corner(matches):
    matching_sides = []
    for i in range(2):
        matching_sides.append(matches[i][1])
    if matching_sides == [0, 1]:
        return '1'
    if matching_sides == [1, 2]:
        return '0'
    if matching_sides == [2, 3]:
        return '3'
    if matching_sides == [3, 0]:
        return '2'
    else:
        print('error in orienting first corner')


# orientation function used only for orienting the first corner. Otherwise obselete
def orient(piece, orientation):
    if 'f' not in orientation:
        orientation = int(orientation)
        for _ in range(orientation):
            piece = rot90(piece)
        return piece
    else:
        orientation = int(orientation[0])
        piece = flip(piece)
        for _ in range(orientation):
            piece = rot90(piece)
        return piece


# orient a piece to put a specific side upwards (to attach to matching side facing down)
# the two orientation functions could easily be optimized and combined, but were separated for maximum clarity
def orient_up(piece, side_to_top, reverse=False):
    if reverse == False:    
        if side_to_top == 1:
            piece = rot90(piece)
            piece = rot90(piece)
            piece = rot90(piece)
        if side_to_top == 2:
            piece = flip(piece)
            piece = rot90(piece)
            piece = rot90(piece)
        if side_to_top == 3:
            piece = flip(piece)
            piece = rot90(piece)
            piece = rot90(piece)
            piece = rot90(piece)

    if reverse == True:
        if side_to_top == 0:
            piece = flip(piece)
        if side_to_top == 1:
            piece = flip(piece)
            piece = rot90(piece)            
        if side_to_top == 2:
            piece = rot90(piece)
            piece = rot90(piece)
        if side_to_top == 3:
            piece = rot90(piece)

    return piece    


# orient a piece to put a specific side to the left (to attach to matching side facing riight)
def orient_left(piece, side_to_left, reverse=False):
    if reverse == False:    
        if side_to_left == 0:
            piece = flip(piece)
            piece = rot90(piece)
            piece = rot90(piece)
            piece = rot90(piece)
        if side_to_left == 1:
            piece = flip(piece)
        if side_to_left == 2:
            piece = rot90(piece)

    if reverse == True:
        if side_to_left == 0:
            piece = rot90(piece)
            piece = rot90(piece)
            piece = rot90(piece)
        if side_to_left == 1:
            piece = rot90(piece)
            piece = rot90(piece)            
        if side_to_left == 2:
            piece = flip(piece)
            piece = rot90(piece)

        if side_to_left == 3:
            piece = flip(piece)
            piece = rot90(piece)
            piece = rot90(piece)

    return piece 


# rotate grid 90 degrees clockwise
def rot90(grid):
    rotatedGrid = copy.deepcopy(grid)
    
    for i in range (0, len(grid)):
        for j in range (0, len(grid)):
            rotatedGrid[i][j] = grid[-(j+1)][i][:]
    return rotatedGrid


# flip grid left to right
def flip(grid):
    for i in range(len(grid)):
        grid[i] = grid[i][::-1]
    return grid
    

if __name__ == "__main__":
    main()